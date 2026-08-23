#!/usr/bin/env python3
"""Language mix across LabbeSimon's own repos, rendered as a stacked bar.

Self-hosted on purpose: no third-party card service between the reader and the
page. Re-run to refresh; the numbers come from the GitHub REST API.

Form per the dataviz skill: part-to-whole -> stacked bar, categorical color,
2px surface gaps, legend + direct labels. Palette validated against #ffffff
and #0d1117.
"""
import json
import os
import urllib.request

USER = "LabbeSimon"

# Third-party code vendored into a repo. GitHub counts it until the repo marks
# it `linguist-vendored` in .gitattributes; drop this entry once it does.
VENDORED = {"G1_Extended": {"C": 1_003_000}}  # liblc3 + rnnoise

FONT = "ui-monospace, SFMono-Regular, 'DejaVu Sans Mono', monospace"
THEMES = {
    "light": dict(ink="#0b0b0b", sec="#52514e", muted="#898781", other="#c3c2b7",
                  hues=["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]),
    "dark": dict(ink="#ffffff", sec="#c3c2b7", muted="#898781", other="#52514e",
                 hues=["#3987e5", "#d95926", "#199e70", "#c98500"]),
}


def get(url):
    headers = {"User-Agent": "profile-readme"}
    token = os.environ.get("GITHUB_TOKEN")  # lifts the anonymous rate limit in CI
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    return json.load(urllib.request.urlopen(req))


def collect():
    totals = {}
    for repo in get(f"https://api.github.com/users/{USER}/repos?per_page=100"):
        if repo["fork"]:
            continue
        langs = get(repo["languages_url"])
        for lang, n in langs.items():
            n -= VENDORED.get(repo["name"], {}).get(lang, 0)
            if n > 0:
                totals[lang] = totals.get(lang, 0) + n
    return totals


def build(totals, mode):
    t = THEMES[mode]
    total = sum(totals.values())
    ranked = sorted(totals.items(), key=lambda kv: -kv[1])
    top = ranked[:4]
    rest = sum(n for _, n in ranked[4:])
    rows = [(name, n, t["hues"][i]) for i, (name, n) in enumerate(top)]
    if rest:
        rows.append(("Other", rest, t["other"]))

    W, BAR_Y, BAR_H, GAP = 900, 30, 26, 2
    parts, x = [], 0.0
    for name, n, hue in rows:
        w = n / total * (W - GAP * (len(rows) - 1))
        parts.append(f'<rect x="{x:.1f}" y="{BAR_Y}" width="{w:.1f}" height="{BAR_H}" rx="2" fill="{hue}"/>')
        pct = n / total * 100
        if w > 90:  # direct label only where it fits inside the segment
            parts.append(
                f'<text x="{x + 12:.1f}" y="{BAR_Y + 18}" font-family="{FONT}" font-size="13" '
                f'font-weight="600" fill="#ffffff">{name} {pct:.0f}%</text>')
        x += w + GAP

    lx = 0.0
    for name, n, hue in rows:
        pct = n / total * 100
        parts.append(f'<rect x="{lx}" y="{BAR_Y + 46}" width="9" height="9" rx="1.5" fill="{hue}"/>')
        label = f"{name} {pct:.1f}%"
        parts.append(
            f'<text x="{lx + 16}" y="{BAR_Y + 55}" font-family="{FONT}" font-size="12.5" '
            f'fill="{t["sec"]}">{label}</text>')
        lx += 16 + len(label) * 7.53 + 26

    parts.append(
        f'<text x="0" y="16" font-family="{FONT}" font-size="12.5" fill="{t["muted"]}">'
        f'Language mix across my own repos · vendored libraries excluded</text>')

    alt = ", ".join(f"{name} {n / total * 100:.1f}%" for name, n, _ in rows)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 100" width="900" '
           f'height="100" role="img" aria-label="Language mix: {alt}">\n  '
           + "\n  ".join(parts) + "\n</svg>\n")
    open(f"langs-{mode}.svg", "w").write(svg)


totals = collect()
print({k: v for k, v in sorted(totals.items(), key=lambda kv: -kv[1])})
for m in THEMES:
    build(totals, m)
print("ok")
