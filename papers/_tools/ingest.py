#!/usr/bin/env python3
"""Ingest downloaded PDFs into the collection.

    python3 papers/_tools/ingest.py [SOURCE_DIR] [--dry-run]

SOURCE_DIR defaults to the parent of papers/ (where browser downloads were saved). For every *.pdf there:
  1. exact duplicates (same SHA-256) are detected;
  2. the PDF is matched to a library paper by DOI (ACM numeric file names, DOIs printed in the first pages)
     and otherwise by title words on the first two pages (match must be unambiguous);
  3. matched files are moved to the paper's expected path (papers/<folder>/<slug>.pdf);
     duplicates, and files for papers that already have a PDF, go to SOURCE_DIR/_duplicates/;
     unmatched files are left in place and reported.
Then run  python3 papers/_tools/build_index.py  (this script does it for you unless --dry-run).
"""
import hashlib, json, os, re, shutil, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = [a for a in sys.argv[1:] if not a.startswith('--')]; DRY = '--dry-run' in sys.argv
SRC = os.path.abspath(args[0]) if args else os.path.dirname(ROOT)
lib = json.load(open(os.path.join(ROOT, '_data', 'library.json')))
by_doi = {(p.get('doi') or '').lower().replace('https://doi.org/', ''): p for p in lib['papers'] if p.get('doi')}
words = lambda s: [w for w in re.sub(r'[^a-z0-9 ]', ' ', (s or '').lower()).split() if len(w) > 3]
def text(f): return subprocess.run(['pdftotext', '-l', '2', f, '-'], capture_output=True, text=True, errors='ignore').stdout
def match(f, txt):
    m = re.match(r'^(\d{7}(?:\.\d{7})?)(?:-\d+)?\.pdf$', os.path.basename(f))
    if m and '10.1145/' + m.group(1) in by_doi: return by_doi['10.1145/' + m.group(1)], 'doi (ACM file name)'
    for d in re.findall(r'10\.\d{4,9}/[^\s"<>]+', txt):
        d = d.rstrip('.,;)').lower()
        if d in by_doi: return by_doi[d], 'doi (in text)'
    # title area = first ~1500 characters of page 1 (title, authors, abstract start) — avoids matching cited titles
    head = set(re.sub(r'[^a-z0-9 ]', ' ', txt[:1500].lower()).split())
    fn = set(re.sub(r'[^a-z0-9 ]', ' ', os.path.basename(f).lower().replace('_', ' ')).split())
    scored = []
    for p in lib['papers']:
        tw = words(p['title'])
        if len(tw) < 3: continue
        s = max(sum(w in head for w in tw) / len(tw), sum(w in fn for w in tw) / len(tw) if len(fn) > 5 else 0)
        # penalise titles whose words cover only a small part of a long, title-like file name
        scored.append((s, len(tw), p))
    scored.sort(key=lambda x: (-x[0], -x[1]))
    if scored and scored[0][0] >= 0.9:
        best = scored[0]; rivals = [x for x in scored[1:] if x[0] >= best[0] - 1e-9 and x[1] == best[1]]
        if not rivals: return best[2], 'title %.2f' % best[0]
    return None, ('no confident match (best: %s %.2f)' % (scored[0][2]['title'][:60], scored[0][0])) if scored else 'no match'
files = sorted(f for f in os.listdir(SRC) if f.lower().endswith('.pdf'))
seen = {}; dup_dir = os.path.join(SRC, '_duplicates'); moved = dups = 0; unmatched = []
for f in files:
    path = os.path.join(SRC, f); data = open(path, 'rb').read()
    if data[:5] != b'%PDF-': unmatched.append((f, 'not a PDF')); continue
    h = hashlib.sha256(data).hexdigest()
    p, how = match(path, text(path))
    if h in seen:
        print(f'DUPLICATE  {f}  (same bytes as {seen[h]})'); dups += 1
        if not DRY: os.makedirs(dup_dir, exist_ok=True); shutil.move(path, os.path.join(dup_dir, f))
        continue
    seen[h] = f
    if not p: unmatched.append((f, how)); continue
    dst = os.path.join(ROOT, p['pdf_expected'])
    if os.path.exists(dst):
        print(f'ALREADY    {f}  -> paper already has {p["pdf_expected"]}'); dups += 1
        if not DRY: os.makedirs(dup_dir, exist_ok=True); shutil.move(path, os.path.join(dup_dir, f))
        continue
    print(f'FILED      {f}\n        -> {p["pdf_expected"]}  [{how}]'); moved += 1
    if not DRY: os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.move(path, dst)
for f, why in unmatched: print(f'UNMATCHED  {f}  ({why})')
print(f'\n{moved} filed, {dups} duplicates/already-present set aside in {dup_dir}, {len(unmatched)} unmatched')
if not DRY and moved: subprocess.run([sys.executable, os.path.join(ROOT, '_tools', 'build_index.py')])
