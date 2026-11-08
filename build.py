"""Bygger markus-portfolio.html (en fil, alla bilder inbakade).

Mall: template.html  ->  resultat: index.html (en fil, alla bilder inbakade)
Källor: img/p/t (thumbs) och img/p/f (stora). Prefix i namnet styr kategori:
  a_  -> action, e_ -> event, v_ -> dok (videos), inget prefix -> portratt
order.json: {"portratt":[...], "action":[...], ...} styr ordningen; bilder som saknas i
order hamnar sist, namn i order som inte finns hoppas över.
"""
import base64, io, json, os, glob
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
PREFIX = {"a_": "action", "e_": "event", "v_": "dok", "x_": "alla"}

def cat_of(n):
    for p, c in PREFIX.items():
        if n.startswith(p): return c
    return "portratt"

def enc(path, maxs, q):
    im = Image.open(path); im.thumbnail((maxs, maxs), Image.LANCZOS)
    b = io.BytesIO(); im.convert("RGB").save(b, "JPEG", quality=q, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

active = json.load(open("active.json"))          # namn som finns i Macens mappar just nu
order = json.load(open("order.json"))
bycat = {}
for n in active:
    bycat.setdefault(cat_of(n), []).append(n)
for c, names in bycat.items():
    pref = list(dict.fromkeys(n for n in order.get(c, []) if n in names))
    bycat[c] = pref + sorted(n for n in names if n not in pref)

# blanda kategorierna i "All": varannan porträtt / action osv
cats = [c for c in ["portratt", "action", "alla", "event", "dok"] if c in bycat]
seq, i = [], 0
while any(i < len(bycat[c]) for c in cats):
    for c in cats:
        if i < len(bycat[c]): seq.append((c, bycat[c][i]))
    i += 1

photos, T, F = [], {}, {}
for c, n in seq:
    w, h = Image.open(f"img/p/t/{n}.jpg").size
    photos.append([c, n, w, h])
    F[n] = enc(f"img/p/f/{n}.jpg", 1300, 76)

s = open("template.html").read()
s = s.replace("/*PHOTOS*/[]", json.dumps(photos, separators=(",", ":")))
s = s.replace("const IMG_T = /*IMG_T*/{};\nconst IMG_F = /*IMG_F*/{};",
              "const IMG_F = " + json.dumps(F, separators=(",", ":")) + ";\nconst IMG_T = IMG_F;")
s = s.replace("__ME__", enc("img/me.jpg", 1000, 80))
open("index.html", "w").write(s)
print({c: len(v) for c, v in bycat.items()}, round(len(s) / 1e6, 1), "MB")
