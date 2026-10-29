"""Render the region blueprint as SVG, using Python's standard library only.

Run: python render_map.py
Reads region-layout.json beside this file; never modifies it or any Unity files.
"""
from pathlib import Path
from html import escape
import json
import math
import random

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "region-layout.json").read_text())
LEFT, TOP, SIZE = 62, 170, 920
SCALE = SIZE / 3000


def xy(point):
    return LEFT + point[0] * SCALE, TOP + SIZE - point[1] * SCALE


def points(items):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in map(xy, items))


parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1200" viewBox="0 0 1600 1200">
<title>Ashen Frontier — The Cinder Basin: precise region blueprint</title>
<desc>Three kilometer square inland post-apocalyptic region. Southwest starter area, western exploration loop, north forest, east dam and quarry, southeast factory. Coordinates are meters, north is up.</desc>
<defs>
  <clipPath id="map"><rect x="62" y="170" width="920" height="920" rx="5"/></clipPath>
  <pattern id="grain" width="32" height="29" patternUnits="userSpaceOnUse"><circle cx="3" cy="5" r=".7" fill="#c9c4a7" opacity=".11"/><circle cx="21" cy="20" r=".6" fill="#c9c4a7" opacity=".07"/></pattern>
  <pattern id="hazard" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(30)"><path d="M0 0V12" stroke="#c8754b" stroke-width="3" opacity=".17"/></pattern>
  <style>
    text { font-family: 'DejaVu Sans', Arial, sans-serif; }
    .micro { font-size:12px; letter-spacing:1.4px; }
    .label { font-size:15px; font-weight:700; letter-spacing:.7px; paint-order:stroke; stroke:#222b28; stroke-width:5px; stroke-linejoin:round; fill:#f3e6c9; }
    .body { font-size:16px; fill:#c4c6b8; }
    .panel-title { font-size:13px; letter-spacing:2px; font-weight:700; fill:#e7ad54; }
  </style>
</defs>
<rect width="1600" height="1200" fill="#171e1d"/>
<text x="62" y="47" class="micro" fill="#e7ad54">ASHEN FRONTIER / WORLD DESIGN 01</text>
<text x="62" y="100" font-size="46" font-weight="700" fill="#f0e6cf" letter-spacing="2">THE CINDER BASIN</text>
<text x="64" y="133" class="body">Stylized survival region · 3 × 3 km · Unity / URP · free-first art direction</text>
<g clip-path="url(#map)">
<rect x="62" y="170" width="920" height="920" fill="#5c604c"/>
''']


def polygon(coords, fill, **attrs):
    extra = " ".join(f'{key.replace("_", "-")}="{value}"' for key, value in attrs.items())
    parts.append(f'<polygon points="{points(coords)}" fill="{fill}" {extra}/>')


def line(coords, color, width, dash=None, opacity=1):
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    parts.append(f'<polyline points="{points(coords)}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" opacity="{opacity}"{extra}/>')


# Broad biomes. These are art regions, not a heightmap or gameplay boundaries.
polygon([[0,0],[800,0],[1240,620],[1100,1250],[410,1600],[0,1300]], "#7b795b")
polygon([[0,1200],[390,1470],[740,2150],[900,3000],[0,3000]], "#727061")
polygon([[930,3000],[1880,3000],[2040,2530],[1800,1920],[1140,1880],[1020,2420]], "#38443a")
polygon([[2260,2850],[3000,3000],[3000,1960],[2440,1970],[2240,2250]], "#9b7853")
polygon([[2240,1030],[3000,1260],[3000,0],[2160,0],[2200,620]], "#655545")
polygon([[2240,1030],[3000,1260],[3000,0],[2160,0],[2200,620]], "url(#hazard)")

# Low contrast contour strokes and forest clusters; fixed seed for repeatability.
rng = random.Random(731)
for cx, cz, radius in [(230,2380,470),(900,2820,330),(2600,2630,460),(1300,300,290)]:
    for ring in range(5):
        rad = radius + ring * 70
        contour = [[cx + math.cos(a)*rad, cz + math.sin(a)*rad*.66] for a in [i*math.pi/24 for i in range(49)]]
        line(contour, "#d5cba5", .7, opacity=.16)
for _ in range(170):
    xz=[rng.uniform(1050,1870),rng.uniform(2050,2910)]
    x,y=xy(xz); h=rng.uniform(5,11)
    parts.append(f'<path d="M{x:.1f} {y+h:.1f}v-{h*1.9:.1f}m0 {h*.5:.1f}l-4 -4m4 8l4 -5" fill="none" stroke="#212d29" stroke-width="1.5"/>')
for _ in range(40):
    x,y=xy([rng.uniform(230,970),rng.uniform(800,1470)])
    parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.8" fill="#4d634a" opacity=".7"/>')

parts.append('<rect x="62" y="170" width="920" height="920" fill="url(#grain)"/>')

# River, floodwater, and planning grid.
line(DATA['water']['river_xz'], '#263f3f', DATA['water']['typical_width_m']*SCALE+5)
line(DATA['water']['river_xz'], '#4b7775', DATA['water']['typical_width_m']*SCALE)
polygon(DATA['water']['flood_polygon_xz'], '#4b7775', stroke="#88aaa0", stroke_width="1", opacity=".9")
for tile in DATA['planning_tiles']:
    x,z=tile['origin_xz']; px,py=xy([x,z+1000])
    parts.append(f'<rect x="{px:.1f}" y="{py:.1f}" width="{1000*SCALE:.1f}" height="{1000*SCALE:.1f}" fill="none" stroke="#e1dcc0" stroke-opacity=".16" stroke-dasharray="4 8"/>')
    parts.append(f'<text x="{px+12:.1f}" y="{py+22:.1f}" class="micro" fill="#d6d6b9" opacity=".55">{tile["id"]}</text>')

# Railway is a visual line, not a walking connection.
line(DATA['railway']['xz'], '#292e29', 5, '3 7')
line(DATA['railway']['xz'], '#b0a081', 1.5)

for route in DATA['routes']:
    state=route['state']; kind=route['kind']
    if state=='later_unlock':
        line(route['xz'], '#de965f', 3, '5 9')
    elif kind=='trail':
        line(route['xz'], '#d1c096', 2.5, '5 5')
    else:
        line(route['xz'], '#363c32', 9)
        line(route['xz'], '#b9aa84', 5)

# Deck and road bridges span the full river.
for crossing in DATA['water']['crossings']:
    cx,cz=crossing['xz']; x,y=xy([cx,cz])
    color='#d7ccad' if crossing['state']=='planned_open' else '#de965f'
    parts.append(f'<path d="M{x-19:.1f} {y:.1f}h38" stroke="#26302b" stroke-width="12"/>')
    parts.append(f'<path d="M{x-19:.1f} {y:.1f}h38" stroke="{color}" stroke-width="6"/>')
    if crossing['state']!='planned_open':
        parts.append(f'<path d="M{x-5:.1f} {y-6:.1f}l10 12m0 -12l-10 12" stroke="#5e3122" stroke-width="3"/>')

# Silhouettes: modern blocks and the paired factory chimneys.
for px,pz in [[1360,1100],[1490,1110],[1580,1060],[1420,950],[1570,940],[1430,1210]]:
    x,y=xy([px,pz]);parts.append(f'<rect x="{x-5:.1f}" y="{y-9:.1f}" width="11" height="18" fill="#828b7d" stroke="#2b4542"/>')
for off in [-90,-40,10,60]:
    line([[1390+off,1770],[1640+off,1560]],'#252b29',2)
for off in [-18,18]:
    x,y=xy([2550,450]);parts.append(f'<rect x="{x+off:.1f}" y="{y-36:.1f}" width="8" height="36" fill="#342b25"/><circle cx="{x+off+4:.1f}" cy="{y-38:.1f}" r="5" fill="#ba7650"/>')

# Starter inset footprint and local two-route loop.
starter=DATA['starter'];lo=starter['bounds_xz']['min'];hi=starter['bounds_xz']['max'];sx,sy=xy([lo[0],hi[1]])
parts.append(f'<rect x="{sx:.1f}" y="{sy:.1f}" width="{600*SCALE:.1f}" height="{600*SCALE:.1f}" rx="4" fill="#e7ad54" fill-opacity=".08" stroke="#e7ad54" stroke-width="2" stroke-dasharray="5 5"/>')
for path in starter['paths']: line(path['xz'],'#e7ad54',2,'3 4')
for item in starter['landmarks']:
    if item['id']=='spawn': continue
    x,y=xy(item['xz']);parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="#e7ad54"/>')
parts.append(f'<text x="{sx+8:.1f}" y="{sy+600*SCALE-10:.1f}" font-size="10" letter-spacing="1" fill="#f2c16f">STARTER / 600 × 600 M</text>')

# Named POIs. Label positions remain derived from coordinates.
for index,poi in enumerate(DATA['pois'],1):
    x,y=xy(poi['xz']); color='#e7ad54' if poi['risk']=='low' else '#eee1bc'
    if poi['risk']=='high':color='#d58d62'
    parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="#242d29" stroke="{color}" stroke-width="2"/>')
    parts.append(f'<text x="{x:.1f}" y="{y+4:.1f}" text-anchor="middle" font-size="11" fill="{color}" font-weight="700">{index:02d}</text>')
    label_y=y+30
    if poi['id']=='cinderhaven':label_y=y-22
    parts.append(f'<text x="{x:.1f}" y="{label_y:.1f}" text-anchor="middle" class="label">{escape(poi["name"].upper())}</text>')
parts.append('</g>')
parts.append('<rect x="62" y="170" width="920" height="920" rx="5" fill="none" stroke="#a3a68c"/>')

# Side panel, generous spacing and explicit build scope.
parts.append('''<path d="M1032 170V1090" stroke="#36413b"/>
<text x="1070" y="192" class="panel-title">REGION AT A GLANCE</text>
<text x="1070" y="229" font-size="27" fill="#f0e6cf">An industrial valley, reclaimed.</text>
<text x="1070" y="262" class="body">A warm outpost. A flooded town. A dead rail yard.</text>
<text x="1070" y="288" class="body">Follow broken infrastructure into the ash zone.</text>
<text x="1070" y="337" class="panel-title">BUILD THE SMALL LOOP FIRST</text>
<rect x="1070" y="356" width="462" height="132" rx="6" fill="#28312b" stroke="#615e3e"/>
<text x="1088" y="387" font-size="20" fill="#f0d298">Cinderhaven → wreck → relay → home</text>
<text x="1088" y="418" class="body">600 × 600 m. One battery. Two walkable routes.</text>
<text x="1088" y="445" class="body">Establish scale, movement and one art sample.</text>
<text x="1088" y="472" class="body">Then expand into the surrounding nine tiles.</text>
<text x="1070" y="534" class="panel-title">WAYFINDING</text>
<path d="M1080 575h54" stroke="#b9aa84" stroke-width="5"/>
<text x="1152" y="580" class="body">Road / planned crossing</text>
<path d="M1080 614h54" stroke="#d1c096" stroke-width="3" stroke-dasharray="5 5"/>
<text x="1152" y="619" class="body">Walking trail</text>
<path d="M1080 653h54" stroke="#de965f" stroke-width="3" stroke-dasharray="5 9"/>
<text x="1152" y="658" class="body">Southern shortcut / later unlock</text>
<path d="M1080 692h54" stroke="#4b7775" stroke-width="12"/>
<text x="1152" y="697" class="body">River / floodwater</text>
<circle cx="1090" cy="733" r="7" stroke="#e7ad54" stroke-width="2" fill="#242d29"/>
<circle cx="1112" cy="733" r="7" stroke="#eee1bc" stroke-width="2" fill="#242d29"/>
<circle cx="1134" cy="733" r="7" stroke="#d58d62" stroke-width="2" fill="#242d29"/>
<text x="1152" y="738" class="body">Risk rises from amber to rust</text>
<text x="1070" y="791" class="panel-title">ART DIRECTION</text>
''')
for i,key in enumerate(['soot','concrete','dust','rust','foliage','water','occupied_light']):
    parts.append(f'<rect x="{1070+i*65}" y="815" width="54" height="25" rx="3" fill="{DATA["palette"][key]}"/>')
parts.append('''<text x="1070" y="873" class="body">Low-poly forms, exposed repairs, charred pines.</text>
<text x="1070" y="900" class="body">Keep saturated warmth around occupied spaces.</text>
<text x="1070" y="947" class="panel-title">UNITY COORDINATES</text>
<text x="1070" y="980" class="body">1 unit = 1 m · +X east · +Z north · +Y up</text>
<text x="1070" y="1007" class="body">Southwest corner: X 0, Z 0</text>
<text x="1070" y="1034" class="body">Grid: nine 1 km planning tiles, A1–C3</text>
<text x="1070" y="1074" font-size="13" fill="#8d9b8e">BLUEPRINT / heights and meshes are separate build tasks.</text>
<text x="62" y="1144" class="micro" fill="#c4c6b8">N ↑</text>
<path d="M130 1130h306m-306 -5v10m153 -10v10m153 -10v10" stroke="#e0d5b8" stroke-width="2"/>
<text x="130" y="1155" font-size="12" fill="#c4c6b8">0</text>
<text x="283" y="1155" text-anchor="middle" font-size="12" fill="#c4c6b8">500</text>
<text x="436" y="1155" text-anchor="end" font-size="12" fill="#c4c6b8">1,000 m</text>
<text x="980" y="1144" text-anchor="end" font-size="13" fill="#8d9b8e">Exact POIs and routes: region-layout.json</text>
<text x="1070" y="1155" class="micro" fill="#8d9b8e">DESIGN CONCEPT · NOT A UNITY BUILD</text>
</svg>''')
(ROOT / "region-map.svg").write_text("\n".join(parts) + "\n")
print("Wrote", ROOT / "region-map.svg")
