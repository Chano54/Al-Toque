"""Junta src/index.html y las librerías de src/lib/ en un solo archivo: index.html (raíz).
Ese archivo es el que publica GitHub Pages y el que se puede mandar o abrir sin internet."""
import pathlib, re
src = pathlib.Path(__file__).parent
html = (src / 'index.html').read_text(encoding='utf-8')
def inline(m):
    code = (src / m.group(1)).read_text(encoding='utf-8')
    assert '</script' not in code.lower()
    return '<script>\n' + code + '\n</script>'
out = re.sub(r'<script src="(lib/[^"]+)"></script>', inline, html)
(src.parent / 'index.html').write_text(out, encoding='utf-8')
print('ok', len(out) // 1024, 'KB')
