GLASSES = [
    "......................",
    "..######......######..",
    ".#......#....#......#.",
    "##......######......##",
    ".#......#....#......#.",
    "..######......######..",
    "......................",
]

DRONE = [
    ".####........####.",
    "...#..........#...",
    "...############...",
    "......#....#......",
    "......#oooo#......",
    "......#.oo.#......",
    ".......####.......",
    "........#.........",
    "......o.....o.....",
    ".....o.......o....",
    "..................",
    "###.##.####.##.###",
]

PAGE = [
    "..############..",
    "..#..........#..",
    "..#.########.#..",
    "..#..........#..",
    "..#.########.#..",
    "..#..........#..",
    "..#.#####....#..",
    "..#..........#..",
    "..#.########.#..",
    "..#..........#..",
    "..############..",
]


def pixels(grid, ox, oy, px, ink, accent):
    out = []
    for y, row in enumerate(grid):
        run_start = None
        for x in range(len(row) + 1):
            ch = row[x] if x < len(row) else "."
            if ch == "#":
                if run_start is None:
                    run_start = x
            else:
                if run_start is not None:
                    out.append(
                        f'<rect x="{ox + run_start * px}" y="{oy + y * px}" '
                        f'width="{(x - run_start) * px}" height="{px}" fill="{ink}"/>'
                    )
                    run_start = None
                if ch == "o":
                    out.append(
                        f'<rect x="{ox + x * px}" y="{oy + y * px}" '
                        f'width="{px}" height="{px}" fill="{accent}"/>'
                    )
    return "\n      ".join(out)


def banner(ink, muted, accent, path):
    px = 5
    art = []
    art.append(pixels(GLASSES, 690, 78, px, ink, accent))
    art.append(pixels(DRONE, 840, 62, px, ink, accent))
    art.append(pixels(PAGE, 980, 65, px, ink, accent))
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 200" width="1100" height="200" role="img" aria-label="Simon Labbe">
  <style>
    .n {{ font: 700 46px ui-monospace, SFMono-Regular, "DejaVu Sans Mono", monospace; fill: {ink}; letter-spacing: 1px; }}
    .t {{ font: 400 19px ui-monospace, SFMono-Regular, "DejaVu Sans Mono", monospace; fill: {muted}; }}
    .k {{ font: 400 19px ui-monospace, SFMono-Regular, "DejaVu Sans Mono", monospace; fill: {accent}; }}
  </style>
  <g>
    <text class="n" x="40" y="88">Simon Labb&#233;</text>
    <text class="t" x="42" y="128">Take out the part everyone assumes is</text>
    <text class="k" x="42" y="160">required<tspan class="t">, then see what still works.</tspan></text>
  </g>
  <g>
      {art[0]}
      {art[1]}
      {art[2]}
  </g>
  <rect x="40" y="176" width="1020" height="2" fill="{muted}" opacity="0.25"/>
</svg>
'''
    open(path, "w").write(svg)


banner("#1f2328", "#59636e", "#0969da", "banner-light.svg")
banner("#e6edf3", "#8b949e", "#58a6ff", "banner-dark.svg")
print("ok")
