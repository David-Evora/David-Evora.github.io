"""Gera versões menores (480, 720, 1200 px) das imagens grandes de assets/img, para o srcset do index.html.
Uso, na raiz do projeto:  python3 tools/make-variants.py   (precisa do Pillow: pip install pillow)
Rode antes de tools/build.py. As imagens originais não são alteradas.
"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")
NAMES = ["hero", "worldskills-competicao", "worldskills-inicio",
         "infofrota-hero-light", "infofrota-hero-dark", "infofrota-dados",
         "infofrota-ia-light", "infofrota-ia-dark", "infofrota-tecnologia", "infofrota-automacao"]
WIDTHS = [480, 720, 1200]

for n in NAMES:
    src = os.path.join(IMG, n + ".webp")
    if not os.path.exists(src):
        print("falta", src); continue
    im = Image.open(src)
    for w in WIDTHS:
        if w >= im.width:
            continue
        h = round(im.height * w / im.width)
        out = os.path.join(IMG, f"{n}-{w}.webp")
        im.convert("RGB").resize((w, h), Image.LANCZOS).save(out, "WEBP", quality=82, method=6)
        print(os.path.basename(out), w, h, os.path.getsize(out) // 1024, "KB")
