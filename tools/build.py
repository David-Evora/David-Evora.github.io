"""Gera index.html a partir de tools/src/. Uso, na raiz do projeto:  python3 tools/build.py

Edite os textos em tools/src/body.html. Cada texto bilíngue usa [[português :: english]].
O CSS e o JavaScript do kit ficam em assets/ (arquivos locais, sem CDN). Sem dependências além do Python 3.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "tools", "src")
FONTS = [("Hanken Grotesk", "hanken-grotesk", "100 900")]


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def expand(html):
    pat = re.compile(r"\[\[(.+?)\s::\s(.+?)\]\]", re.S)
    out = pat.sub(lambda m: f'<span lang="pt-BR">{m.group(1).strip()}</span><span lang="en">{m.group(2).strip()}</span>', html)
    assert "[[" not in out and "]]" not in out, "marcador [[ ]] sem par em body.html"
    return out


def font_css():
    return "\n".join(
        f'@font-face{{font-family:"{fam}";font-style:normal;font-weight:{w};font-display:swap;src:url(assets/fonts/{pkg}-latin-wght-normal.woff2) format("woff2")}}'
        for fam, pkg, w in FONTS)


# imagens com versões menores (tools/make-variants.py): ganham srcset; as demais ficam como estão
HALF = ("hero", "worldskills-competicao", "worldskills-inicio", "infofrota-hero-light", "infofrota-hero-dark")
SIZES_THUMB = "(max-width: 767px) 280px, 300px"
THUMBS = ("cert-java", "cert-kaggle", "cert-oracle")
SIZES_HALF = "(max-width: 767px) calc(100vw - 48px), 640px"
SIZES_WIDE = "(max-width: 767px) calc(100vw - 48px), 1280px"


def add_srcset(html):
    def sub(m):
        name = m.group(2)
        found = [w for w in (480, 720, 1200) if os.path.exists(os.path.join(ROOT, "assets", "img", f"{name}-{w}.webp"))]
        if not found or "srcset=" in m.group(0):
            return m.group(0)
        full = Image_width(name)
        cands = ", ".join([f"assets/img/{name}-{w}.webp {w}w" for w in found] + [f"assets/img/{name}.webp {full}w"])
        sizes = SIZES_THUMB if name in THUMBS else (SIZES_HALF if name in HALF else SIZES_WIDE)
        return f'{m.group(1)}src="assets/img/{name}.webp" srcset="{cands}" sizes="{sizes}"'
    return re.sub(r'(<img\b[^>]*?)src="assets/img/([a-z0-9-]+)\.webp"', sub, html)


def Image_width(name):
    # largura real do arquivo original, lida do cabeçalho WebP via Pillow
    from PIL import Image
    with Image.open(os.path.join(ROOT, "assets", "img", name + ".webp")) as im:
        return im.width


ICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect width='24' height='24' rx='5' fill='%230b0c0e'/%3E"
        "%3Cpath fill='%23eef0f3' fill-rule='evenodd' d='M12 4.5a7.5 7.5 0 1 1 0 15 7.5 7.5 0 0 1 0-15zm0 4.1a3.4 3.4 0 1 0 0 6.8 3.4 3.4 0 0 0 0-6.8z'/%3E%3C/svg%3E")


def main():
    head = read(f"{SRC}/head.html").replace("@@FONTS@@", font_css())
    body = add_srcset(expand(read(f"{SRC}/body.html")))
    scripts = ('<script type="module" src="assets/system.js"></script>\n'
               '<script type="module" src="assets/motion/motion.js"></script>\n'
               '<script type="module" src="assets/layout/layout.js"></script>\n'
               f"<script>\n{read(f'{SRC}/app.js')}</script>\n")
    doc = ('<!doctype html>\n<html lang="pt-BR" data-type="service" data-radius="soft" data-buttons="tonal" data-motion>\n<head>\n<meta charset="utf-8">\n'
           '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
           '<meta name="color-scheme" content="light dark">\n'
           f'<link rel="icon" href="{ICON}">\n' + head + '\n</head>\n<body id="top">\n' + body + scripts + "</body>\n</html>\n")
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    print("index.html", len(doc) // 1024, "KB")


if __name__ == "__main__":
    main()
