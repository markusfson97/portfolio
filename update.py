"""Läser bildmapparna i "Markus hemsida", gör webbversioner av nya bilder och bygger om sidan.

Kör:  python3 update.py
Kräver: pip install pillow

Mappar (ligger en nivå upp från den här kodmappen):
  Portraits      -> fliken Portraits
  Action sports  -> fliken Action sports
  Alla           -> visas bara under fliken All
Bilder som raderas ur mapparna försvinner från sidan, nya läggs till sist i sin flik
(ordningen styrs av order.json).
"""
import glob, json, os, re, subprocess, sys
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # mappen "Markus hemsida"
FOLDERS = {"Portraits": "", "Action sports": "a_", "Alla": "x_"}
EXT = (".jpg", ".jpeg", ".png")

def slug(fn):
    return re.sub(r"[^a-z0-9]", "", os.path.splitext(fn)[0].lower())

os.makedirs(os.path.join(HERE, "img/p/t"), exist_ok=True)
os.makedirs(os.path.join(HERE, "img/p/f"), exist_ok=True)

active, new = [], []
for folder, prefix in FOLDERS.items():
    for path in sorted(glob.glob(os.path.join(ROOT, folder, "*"))):
        if not path.lower().endswith(EXT):
            continue
        n = prefix + slug(os.path.basename(path))
        active.append(n)
        full = os.path.join(HERE, f"img/p/f/{n}.jpg")
        if os.path.exists(full) and os.path.getmtime(full) >= os.path.getmtime(path):
            continue
        im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
        a = im.copy(); a.thumbnail((1500, 1500), Image.LANCZOS); a.save(full, quality=80, optimize=True)
        b = im.copy(); b.thumbnail((640, 640), Image.LANCZOS)
        b.save(os.path.join(HERE, f"img/p/t/{n}.jpg"), quality=74, optimize=True)
        new.append(n)

json.dump(active, open(os.path.join(HERE, "active.json"), "w"))
print(f"{len(active)} bilder totalt, {len(new)} nya: {new}")
subprocess.run([sys.executable, os.path.join(HERE, "build.py")], check=True)
