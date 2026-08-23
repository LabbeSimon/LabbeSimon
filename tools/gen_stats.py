# KPI row — three stat tiles, one per project.
# Form per dataviz skill: "a handful of headline numbers" -> KPI row of stat
# tiles, not a grouped bar chart. Palette validated with
# scripts/validate_palette.py against #ffffff and #0d1117 (GitHub surfaces).

THEMES = {
    "light": dict(
        ink="#0b0b0b", sec="#52514e", muted="#898781", rule="#e1e0d9",
        c1="#2a78d6", c2="#eb6834", c3="#1baf7a", ghost="#f4c3a9",
    ),
    "dark": dict(
        ink="#ffffff", sec="#c3c2b7", muted="#898781", rule="#2c2c2a",
        c1="#3987e5", c2="#d95926", c3="#199e70", ghost="#6e3d29",
    ),
}

TILES = [
    dict(key="c1", name="G1 Extended", value="0",
         cap=["no account, no server, no byte",
              "of telemetry leaving the phone"],
         foot="two BLE radios, driven directly"),
    dict(key="c2", name="CMS", value="2",
         cap=["blocking requests before paint,",
              "whatever the plugin count"],
         foot=None),
    dict(key="c3", name="VectorFix", value="3000×",
         cap=["less storage to cover France:",
              "1–3 GB of vector, not 5–10 TB"],
         foot="on an ESP32-S3, at ~0.5 W"),
]

FONT = "ui-monospace, SFMono-Regular, 'DejaVu Sans Mono', monospace"


def dumbbell(x, y, w, t):
    """Before -> after on one axis. 1 hue, 2 shades, both ends labelled."""
    lo, hi = 0.0, 32.0
    px = lambda v: x + (v - lo) / (hi - lo) * w
    a, b = px(2), px(30)
    return f'''
    <line x1="{x}" y1="{y}" x2="{x + w}" y2="{y}" stroke="{t['rule']}" stroke-width="1"/>
    <line x1="{a}" y1="{y}" x2="{b}" y2="{y}" stroke="{t['c2']}" stroke-width="2" opacity="0.45"/>
    <circle cx="{b}" cy="{y}" r="5" fill="{t['ghost']}"/>
    <circle cx="{a}" cy="{y}" r="5" fill="{t['c2']}"/>
    <text x="{b}" y="{y - 11}" text-anchor="middle" font-family="{FONT}" font-size="11.5" fill="{t['muted']}">30</text>
    <text x="{a}" y="{y - 11}" text-anchor="middle" font-family="{FONT}" font-size="11.5" fill="{t['sec']}">2</text>
    <text x="{x}" y="{y + 22}" font-family="{FONT}" font-size="11.5" fill="{t['muted']}">WordPress, 15 plugins → this</text>'''


def build(mode):
    t = THEMES[mode]
    tw, gap = 280, 30
    parts = []
    for i, tile in enumerate(TILES):
        x = i * (tw + gap)
        hue = t[tile["key"]]
        parts.append(f'<rect x="{x}" y="0" width="34" height="3" fill="{hue}"/>')
        parts.append(f'<text x="{x}" y="30" font-family="{FONT}" font-size="14" font-weight="600" fill="{t["sec"]}">{tile["name"]}</text>')
        parts.append(f'<text x="{x}" y="80" font-family="{FONT}" font-size="38" font-weight="700" fill="{t["ink"]}">{tile["value"]}</text>')
        for j, line in enumerate(tile["cap"]):
            parts.append(f'<text x="{x}" y="{106 + j * 19}" font-family="{FONT}" font-size="13" fill="{t["muted"]}">{line}</text>')
        if tile["foot"]:
            parts.append(f'<text x="{x}" y="163" font-family="{FONT}" font-size="11.5" fill="{t["sec"]}" opacity="0.8">{tile["foot"]}</text>')
        if tile["name"] == "CMS":
            parts.append(dumbbell(x, 156, 190, t))
    body = "\n  ".join(parts)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 190" width="900" height="190" role="img" aria-label="G1 Extended: 0 accounts or telemetry. CMS: 2 blocking requests at any plugin count, down from 30. VectorFix: 3000 times less storage to cover France.">
  {body}
</svg>
'''
    open(f"stats-{mode}.svg", "w").write(svg)


for m in THEMES:
    build(m)
print("ok")
