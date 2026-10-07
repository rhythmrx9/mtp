#!/usr/bin/env python3
"""Generate papers/agents/ — the navigation index for AI agents — from _data/library.json.
Called automatically at the end of build_index.py. Hand-written files (AGENTS.md, agents/glossary.md,
agents/schema.md) are NOT touched; everything else under agents/ is regenerated."""
import json, os, re, shutil, subprocess, datetime, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, 'agents')
lib = json.load(open(os.path.join(ROOT, '_data', 'library.json')))
P = {p['id']: p for p in lib['papers']}; CAT = {c['id']: c for c in lib['categories']}
for d in ('cards', 'fulltext', 'topics', 'categories', 'facets'):
    os.makedirs(os.path.join(A, d), exist_ok=True)
slug = lambda p: os.path.splitext(os.path.basename(p['pdf_expected']))[0]
S = {pid: slug(p) for pid, p in P.items()}
out_e = collections.defaultdict(list); in_e = collections.defaultdict(list)
for e in lib['edges']:
    if e['s'] in P and e['t'] in P: out_e[e['s']].append(e); in_e[e['t']].append(e)
def has_pdf(p): return os.path.exists(os.path.join(ROOT, p['pdf_expected']))
def one(s): return re.sub(r'\s+', ' ', str(s or '')).strip()
def yq(s): return json.dumps(one(s), ensure_ascii=False)
prio = lambda p: p.get('priority') or 0
ordered = sorted(lib['papers'], key=lambda p: (p['cat'], -prio(p)))

# ---- full text (page-delimited) ----
ft_have = set()
for p in lib['papers']:
    if not has_pdf(p): continue
    pdf = os.path.join(ROOT, p['pdf_expected']); txt = os.path.join(A, 'fulltext', S[p['id']] + '.txt')
    if not os.path.exists(txt) or os.path.getmtime(txt) < os.path.getmtime(pdf):
        raw = subprocess.run(['pdftotext', '-enc', 'UTF-8', pdf, '-'], capture_output=True, text=True, errors='ignore').stdout
        pages = raw.split('\f')
        with open(txt, 'w') as f:
            f.write(f'# {p["title"]}\n# id: {p["id"]} | key: {S[p["id"]]} | {p.get("venue_short","")} {p.get("year","")} | card: ../cards/{S[p["id"]]}.md\n\n')
            for i, pg in enumerate(pages, 1):
                if pg.strip(): f.write(f'\n=== page {i} ===\n{pg.strip()}\n')
    ft_have.add(p['id'])
for f in os.listdir(os.path.join(A, 'fulltext')):   # drop stale files
    if f[:-4] not in S.values(): os.remove(os.path.join(A, 'fulltext', f))

# ---- per-paper cards ----
for f in os.listdir(os.path.join(A, 'cards')):
    if f[:-3] not in S.values(): os.remove(os.path.join(A, 'cards', f))
for p in lib['papers']:
    k = S[p['id']]; c = CAT[p['cat']]
    fm = ['---', f'id: {p["id"]}', f'key: {k}', f'title: {yq(p["title"])}', f'short: {yq(p.get("short"))}',
          f'year: {p.get("year")}', f'venue: {yq(p.get("venue_short") or p.get("venue"))}', f'venue_full: {yq(p.get("venue_full") or p.get("venue"))}',
          f'authors: {yq(", ".join((p.get("authors") or [])[:12]) + (" et al." if len(p.get("authors") or []) > 12 else ""))}',
          f'category: "{p["cat"]} {c["name"]}"', f'devices: {json.dumps(p.get("devices") or [])}', f'models: {json.dumps(p.get("models") or [])}',
          f'lm_models: {json.dumps(p.get("lm_models") or [], ensure_ascii=False)}', f'param_scale: {yq(p.get("param_scale"))}', f'slm: {str(bool(p.get("slm"))).lower()}',
          f'evidence: {p.get("evidence","unknown")}', f'topics: {json.dumps(p.get("topics") or [])}',
          f'analysis_basis: {p.get("basis") or "unknown"}', f'in_original_review: {str(bool(p.get("seed"))).lower()}',
          f'cited_by_in_collection: {len(in_e[p["id"]])}', f'cites_in_collection: {len(out_e[p["id"]])}', f'citations_overall: {p.get("cites_global") or 0}',
          f'priority_score: {prio(p)}', f'doi: {yq(p.get("doi"))}',
          f'pdf: {yq("../../" + p["pdf_expected"]) if has_pdf(p) else "null"}', f'fulltext: {yq("../fulltext/" + k + ".txt") if p["id"] in ft_have else "null"}', '---', '']
    b = [f'# {p.get("short") or p["title"]}', '', f'**{p["title"]}** — {p.get("venue_full") or p.get("venue","")} ({p.get("year")})', '']
    if p.get('basis') != 'full-text':
        b += ['> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.', '']
    b += ['## TL;DR', one(p.get('tldr')), '', '## Summary', one(p.get('summary')), '']
    if p.get('lm_models') or p.get('slm_note'):
        b += ['## Language models evaluated', f'- Models: {", ".join(p.get("lm_models") or []) or "—"}', f'- Scale: {p.get("param_scale") or "—"}'] + ([f'- Note: {one(p["slm_note"])}'] if p.get('slm_note') else []) + ['']
    if p.get('contributions'): b += ['## Contributions'] + [f'- {one(x)}' for x in p['contributions']] + ['']
    if p.get('claims'):
        b += ['## Key claims (stable IDs)']
        for i, cl in enumerate(p['claims'], 1):
            b.append(f'- **{k}#C{i}** — {one(cl.get("claim"))}' + (f' — _support:_ {one(cl.get("support"))}' if cl.get('support') else '') + (f' — _loc:_ {one(cl.get("loc"))}' if cl.get('loc') else ''))
        b.append('')
    if p.get('results'): b += ['## Results'] + [f'- {one(x)}' for x in p['results']] + ['']
    kn = {kk: vv for kk, vv in (p.get('key_numbers') or {}).items() if vv}
    if kn: b += ['## Key numbers'] + [f'- {kk}: {one(vv)}' for kk, vv in kn.items()] + ['']
    if p.get('datasets_benchmarks'): b += ['## Datasets / benchmarks', ', '.join(p['datasets_benchmarks']), '']
    if p.get('limitations'): b += ['## Limitations'] + [f'- {one(x)}' for x in p['limitations']] + ['']
    if p.get('remarks'): b += ['## Remarks', one(p['remarks']), '']
    if p.get('review'):
        b += ['## Use in the original review'] + [f'- {f["fid"]} ({f.get("grade","")}): {one(f.get("text"))}' for f in p['review']] + ['']
    if out_e[p['id']]:
        b += [f'## Cites (in collection, {len(out_e[p["id"]])})']
        for e in sorted(out_e[p['id']], key=lambda e: -bool(e.get('ctx'))):
            q = P[e['t']]; b.append(f'- [{S[q["id"]]}]({S[q["id"]]}.md) {q.get("short") or q["title"][:60]} ({q.get("year")})' + (f' — _{e["purpose"]}_' if e.get('purpose') else '') + (f': "{one(e["ctx"])}"' if e.get('ctx') else ''))
        b.append('')
    if in_e[p['id']]:
        b += [f'## Cited by (in collection, {len(in_e[p["id"]])})']
        for e in sorted(in_e[p['id']], key=lambda e: -bool(e.get('ctx'))):
            q = P[e['s']]; b.append(f'- [{S[q["id"]]}]({S[q["id"]]}.md) {q.get("short") or q["title"][:60]} ({q.get("year")})' + (f' — _{e["purpose"]}_' if e.get('purpose') else '') + (f': "{one(e["ctx"])}"' if e.get('ctx') else ''))
        b.append('')
    b += ['## Files', f'- PDF: ' + (f'[../../{p["pdf_expected"]}](../../{p["pdf_expected"]})' if has_pdf(p) else f'not available locally (save as `papers/{p["pdf_expected"]}`)'),
          f'- Full text: ' + (f'[../fulltext/{k}.txt](../fulltext/{k}.txt) (page markers `=== page N ===`)' if p['id'] in ft_have else 'none'),
          f'- DOI: {p.get("doi") or "—"}', '']
    open(os.path.join(A, 'cards', k + '.md'), 'w').write('\n'.join(fm + b))

# ---- machine-readable indexes ----
with open(os.path.join(A, 'catalog.jsonl'), 'w') as f:
    for p in ordered:
        f.write(json.dumps({'id': p['id'], 'key': S[p['id']], 'short': p.get('short'), 'title': p['title'], 'year': p.get('year'),
            'venue': p.get('venue_short') or p.get('venue'), 'cat': p['cat'], 'devices': p.get('devices') or [], 'models': p.get('models') or [],
            'lm_models': p.get('lm_models') or [], 'param_scale': p.get('param_scale') or '', 'slm': bool(p.get('slm')), 'evidence': p.get('evidence'),
            'topics': p.get('topics') or [], 'basis': p.get('basis'), 'seed': bool(p.get('seed')), 'cited_by_n': len(in_e[p['id']]),
            'cites_n': len(out_e[p['id']]), 'citations_overall': p.get('cites_global') or 0, 'priority': prio(p), 'tldr': one(p.get('tldr')),
            'card': f'cards/{S[p["id"]]}.md', 'fulltext': f'fulltext/{S[p["id"]]}.txt' if p['id'] in ft_have else None,
            'pdf': f'../{p["pdf_expected"]}' if has_pdf(p) else None, 'doi': p.get('doi')}, ensure_ascii=False) + '\n')
with open(os.path.join(A, 'claims.jsonl'), 'w') as f:
    for p in ordered:
        for i, cl in enumerate(p.get('claims') or [], 1):
            f.write(json.dumps({'claim_id': f'{S[p["id"]]}#C{i}', 'paper': p['id'], 'key': S[p['id']], 'year': p.get('year'), 'cat': p['cat'],
                'evidence': p.get('evidence'), 'basis': p.get('basis'), 'claim': one(cl.get('claim')), 'support': one(cl.get('support')), 'loc': one(cl.get('loc'))}, ensure_ascii=False) + '\n')
with open(os.path.join(A, 'citations.jsonl'), 'w') as f:
    for e in lib['edges']:
        if e['s'] in P and e['t'] in P:
            f.write(json.dumps({'from': e['s'], 'from_key': S[e['s']], 'to': e['t'], 'to_key': S[e['t']], 'purpose': e.get('purpose') or '', 'context': one(e.get('ctx'))}, ensure_ascii=False) + '\n')

# ---- human/agent-readable tables of contents ----
row = lambda p: f'| [{S[p["id"]]}](cards/{S[p["id"]]}.md) | {p.get("year")} | {p.get("venue_short","")} | {p["cat"]} | {",".join(p.get("devices") or [])} | {p.get("evidence","")} | {"F" if p.get("basis")=="full-text" else "A"} | {len(in_e[p["id"]])} | {one(p.get("tldr"))[:160].replace("|","/")} |'
hdr = ['| key (→ card) | year | venue | cat | devices | evidence | basis | cited-by | TL;DR |', '|---|---|---|---|---|---|---|---|---|']
open(os.path.join(A, 'catalog.md'), 'w').write('\n'.join(['# Catalog — every paper, one line each', '',
    'Sorted by category, then importance. basis: F = analysed from full text, A = abstract only. cited-by = citations from other papers in this collection. Open a card for details; grep `catalog.jsonl` for structured filtering.', ''] + hdr + [row(p) for p in ordered]) + '\n')
for f in os.listdir(os.path.join(A, 'categories')): os.remove(os.path.join(A, 'categories', f))
for cid, c in CAT.items():
    ps = [p for p in ordered if p['cat'] == cid]
    open(os.path.join(A, 'categories', f'{c["dir"]}.md'), 'w').write('\n'.join([f'# {cid} · {c["name"]}', '', c['desc'], '',
        f'{len(ps)} papers ({sum(has_pdf(p) for p in ps)} with PDF). Ordered by importance (priority score). Folder: `papers/{c["dir"]}/`.', ''] +
        [h.replace('cards/', '../cards/') for h in hdr] + [row(p).replace('](cards/', '](../cards/') for p in ps]) + '\n')
topics = collections.defaultdict(list)
for p in ordered:
    for t in p.get('topics') or []: topics[t].append(p)
for f in os.listdir(os.path.join(A, 'topics')): os.remove(os.path.join(A, 'topics', f))
for t, ps in topics.items():
    ps = sorted(ps, key=lambda p: -prio(p))
    open(os.path.join(A, 'topics', t + '.md'), 'w').write('\n'.join([f'# Topic: {t}', '', f'{len(ps)} papers, most important first.', ''] +
        [h.replace('cards/', '../cards/') for h in hdr] + [row(p).replace('](cards/', '](../cards/') for p in ps]) + '\n')
open(os.path.join(A, 'topics', 'INDEX.md'), 'w').write('\n'.join(['# Topic index', '', 'Controlled vocabulary assigned per paper (see ../schema.md). Count = papers tagged.', ''] +
    [f'- [{t}]({t}.md) — {len(ps)}' for t, ps in sorted(topics.items(), key=lambda x: -len(x[1]))]) + '\n')
def facet(name, key, title):
    groups = collections.defaultdict(list)
    for p in ordered:
        vals = p.get(key) or []
        vals = vals if isinstance(vals, list) else [vals]
        for v in vals or ['(none)']: groups[v].append(p)
    lines = [f'# {title}', '']
    for v, ps in sorted(groups.items(), key=lambda x: -len(x[1])):
        ps = sorted(ps, key=lambda p: -prio(p))
        lines += [f'## {v} ({len(ps)})', ''] + [f'- [{S[p["id"]]}](../cards/{S[p["id"]]}.md) — {one(p.get("tldr"))[:140]}' for p in ps] + ['']
    open(os.path.join(A, 'facets', name + '.md'), 'w').write('\n'.join(lines))
facet('devices', 'devices', 'Papers by memory device / technology'); facet('models', 'models', 'Papers by workload model family')
facet('language_models', 'lm_models', 'Papers by specific language model evaluated'); facet('evidence', 'evidence', 'Papers by evidence type')
facet('venues', 'venue_short', 'Papers by venue'); facet('years', 'year', 'Papers by year')
f_lines = ['# Findings of the original review (F = verified, R = refuted, N = unadjudicated)', '']
for fd in lib.get('findings', []):
    ps = [p for p in lib['papers'] if any(r['fid'] == fd['fid'] for r in p.get('review') or [])]
    f_lines += [f'## {fd["fid"]} — {fd.get("grade","")} {fd.get("vote","")}', one(fd.get('text')), '', (f'_Note:_ {one(fd["note"])}' if fd.get('note') else ''),
                'Papers: ' + (', '.join(f'[{S[p["id"]]}](cards/{S[p["id"]]}.md)' for p in ps) or 'source not in collection'), '']
open(os.path.join(A, 'review_findings.md'), 'w').write('\n'.join(f_lines))

# ---- llms.txt entry point ----
top = sorted(lib['papers'], key=lambda p: -prio(p))[:30]
n_ft = sum(1 for p in lib['papers'] if p.get('basis') == 'full-text'); n_pdf = sum(has_pdf(p) for p in lib['papers'])
L = [f'# Analog AI Hardware Paper Collection', '',
     f'> {len(P)} peer-reviewed papers on running AI models — from CNNs to transformers and small language models — on analog / non-volatile in-memory computing hardware (PCM, ReRAM, FeFET, MRAM, charge/gain-cell CIM), and on mapping models onto crossbar arrays. Every paper has a structured card (summary, claims with stable IDs, results, limitations, remarks, citation contexts); {n_pdf} have local PDFs and page-marked full text.', '',
     'Read ../AGENTS.md first for search recipes and citation rules. Prefer grep over reading whole files: catalog.jsonl (1 line/paper), claims.jsonl (1 line/claim), citations.jsonl (1 line/citation with the citing sentence).', '',
     '## Start here', '- [AGENTS.md](../AGENTS.md): how to navigate, search recipes, citation rules',
     '- [catalog.md](catalog.md): every paper on one line (key, year, venue, category, devices, evidence, TL;DR)',
     '- [schema.md](schema.md): field definitions and controlled vocabularies', '- [glossary.md](glossary.md): domain terms, abbreviations and search synonyms', '',
     '## Categories'] + [f'- [{c["dir"]}](categories/{c["dir"]}.md): {c["name"]} — {sum(1 for p in P.values() if p["cat"]==cid)} papers' for cid, c in CAT.items()] + ['',
     '## Most important papers'] + [f'- [{S[p["id"]]}](cards/{S[p["id"]]}.md): {one(p.get("tldr"))[:150]}' for p in top] + ['',
     '## Indexes', '- [topics/INDEX.md](topics/INDEX.md): papers by topic tag', '- [facets/devices.md](facets/devices.md): by device technology',
     '- [facets/language_models.md](facets/language_models.md): by language model evaluated', '- [facets/models.md](facets/models.md): by workload family',
     '- [facets/evidence.md](facets/evidence.md): measured silicon vs simulation vs survey', '- [review_findings.md](review_findings.md): verified/refuted findings of the seed review', '',
     '## Optional', '- [catalog.jsonl](catalog.jsonl): structured catalog for filtering', '- [claims.jsonl](claims.jsonl): every key claim with support and location',
     '- [citations.jsonl](citations.jsonl): citation graph with citing sentences', '- [fulltext/](fulltext/): page-marked full text for verification', '- [facets/venues.md](facets/venues.md), [facets/years.md](facets/years.md)', '- [../_data/missing_pdfs.md](../_data/missing_pdfs.md): papers without PDFs, ranked by priority']
open(os.path.join(A, 'llms.txt'), 'w').write('\n'.join(L) + '\n')
json.dump({'generated': datetime.datetime.now().isoformat(timespec='seconds'), 'papers': len(P), 'with_pdf': n_pdf, 'full_text_analyses': n_ft,
           'abstract_only_analyses': len(P) - n_ft, 'citation_links': len(lib['edges']), 'with_citing_sentence': sum(1 for e in lib['edges'] if e.get('ctx')),
           'claims': sum(len(p.get('claims') or []) for p in P.values()), 'categories': {cid: sum(1 for p in P.values() if p['cat']==cid) for cid in CAT},
           'topics': {t: len(v) for t, v in sorted(topics.items(), key=lambda x: -len(x[1]))}}, open(os.path.join(A, 'manifest.json'), 'w'), indent=1)
print(f'agents/: {len(P)} cards, {len(ft_have)} full texts, {sum(len(p.get("claims") or []) for p in P.values())} claims, {len(topics)} topics')
