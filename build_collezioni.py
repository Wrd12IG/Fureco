#!/usr/bin/env python3
"""
Genera collezioni-donna.html con tutti i prodotti dal catalogo Excel.
Percorso immagini: prodotti/CATEGORIA/CODICE_A.jpg
"""
import openpyxl
import os

SITE = '/Volumes/Archivio/FURECO/BRAND/materiale sito'
EXCEL = '/Volumes/Archivio/FURECO/FOTO SITO/PRODOTTI CON DESCRIZIONI.xlsx'
PRODOTTI_DIR = os.path.join(SITE, 'prodotti')

CAT_MAP = {
    'CHINCHILLA':                   ('CHINCHILLA', 'Cincillà'),
    'MINK':                         ('MINK',       'Visone'),
    'SABLE':                        ('SABLE',       'Zibellino'),
    'SHEARLING':                    ('SHEARLING',   'Shearling'),
    'FOX':                          ('FOX',         'Volpe'),
    'LORO PIANA CASHMERE WITH FUR': ('LORO-PIANA',  'Cashmere Loro Piana'),
}

# ── leggi Excel ──────────────────────────────────────────────────────────────
wb = openpyxl.load_workbook(EXCEL, data_only=True)
ws = wb.active

products = []
current_cat = None

for row in ws.iter_rows(values_only=True):
    code = str(row[0]).strip() if row[0] else ''
    desc = str(row[1]).strip() if row[1] else ''
    if not code:
        continue
    if code in CAT_MAP or code == 'CODE':
        current_cat = code
        continue
    folder, label = CAT_MAP.get(current_cat, ('', ''))
    # trova immagine _A.jpg o _B.jpg
    img_a = f'prodotti/{folder}/{code}_A.jpg'
    img_b = f'prodotti/{folder}/{code}_B.jpg'
    img_path_a = os.path.join(SITE, img_a)
    img_path_b = os.path.join(SITE, img_b)
    img = img_a if os.path.exists(img_path_a) else (img_b if os.path.exists(img_path_b) else '')
    # prima riga della descrizione = nome capo
    first_line = desc.split('\n')[0].strip() if desc else ''
    name = first_line if first_line and not first_line.startswith('•') else code
    # rimuovi righe che iniziano con • per il teaser
    teaser_lines = [l for l in desc.split('\n') if l.strip() and not l.strip().startswith('•') and l.strip() != first_line]
    teaser = ' '.join(teaser_lines).strip()[:180] + ('…' if len(' '.join(teaser_lines)) > 180 else '')
    products.append({
        'code': code,
        'category': current_cat,
        'folder': folder,
        'label': label,
        'img': img,
        'name': name,
        'desc': desc,
        'teaser': teaser,
    })

total = len(products)
print(f'Prodotti trovati: {total}')

# ── genera card HTML ──────────────────────────────────────────────────────────
def make_card(p):
    img_tag = f'<img src="{p["img"]}" alt="{p["name"]} {p["code"]}" loading="lazy" />' if p["img"] else '<div style="width:100%;height:100%;background:var(--bone);display:flex;align-items:center;justify-content:center;color:var(--gray-3);font-family:JetBrains Mono,monospace;font-size:10px;">IMMAGINE<br>IN ARRIVO</div>'
    data_cat = p['category'].lower().replace(' ', '-')
    return f'''      <a class="product-card" href="wireframe-v4-PRODOTTO.html" data-cat="{data_cat}">
        <div class="product-img-wrap">{img_tag}</div>
        <div class="product-info">
          <p class="product-code">{p["code"]}</p>
          <p class="product-name">{p["name"]}</p>
          <p class="product-material">{p["label"]} · Made in Italy</p>
          <div class="product-action">
            <span class="product-cta">Scopri il capo &rarr;</span>
            <span class="product-wishlist">&#9825;</span>
          </div>
        </div>
      </a>'''

cards_html = '\n'.join(make_card(p) for p in products)

# ── filtri unici ──────────────────────────────────────────────────────────────
seen = []
filter_btns = ['<button class="filter-btn active" data-filter="all">Tutti</button>']
for p in products:
    cat = p['category']
    if cat not in seen:
        seen.append(cat)
        slug = cat.lower().replace(' ', '-')
        filter_btns.append(f'<button class="filter-btn" data-filter="{slug}">{p["label"]}</button>')
filters_html = '\n  '.join(filter_btns)

# ── HTML completo ─────────────────────────────────────────────────────────────
html = f'''<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Collezioni Donna — Fabio Gavazzi | Fureco</title>
  <meta name="description" content="Scopri la collezione donna Fabio Gavazzi FW 2025: {total} capi in cincillà, visone, zibellino, shearling e cashmere Loro Piana. Artigianato italiano dal 1924." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --bordeaux:#6d212b; --paper:#fafaf8; --bone:#f5f3ef; --ink:#1f1d1a;
      --tortora:#b8aa97; --line:#e8e5df; --gray-1:#4a4844; --gray-2:#7a766f;
      --gray-3:#a8a39a; --white:#ffffff;
    }}
    *, *::before, *::after {{ box-sizing:border-box; margin:0; padding:0; }}
    html {{ scroll-behavior:smooth; }}
    body {{ font-family:'Inter',sans-serif; background:var(--paper); color:var(--ink); -webkit-font-smoothing:antialiased; }}
    img {{ display:block; max-width:100%; }}
    a {{ color:inherit; text-decoration:none; }}
    ul {{ list-style:none; }}

    .utility-bar {{ display:flex; align-items:center; justify-content:space-between; background:var(--bone); border-bottom:1px solid var(--line); color:var(--gray-2); padding:10px 48px; font-family:'JetBrains Mono',monospace; font-size:10px; letter-spacing:.18em; text-transform:uppercase; }}
    .utility-bar a {{ color:var(--bordeaux); }}
    .main-nav {{ display:flex; align-items:center; justify-content:space-between; background:var(--white); border-bottom:1px solid var(--line); padding:0 48px; height:72px; position:sticky; top:0; z-index:100; }}
    .nav-left, .nav-right {{ display:flex; align-items:center; gap:32px; }}
    .nav-item {{ font-family:'Inter',sans-serif; font-size:11px; font-weight:500; letter-spacing:.15em; text-transform:uppercase; color:var(--gray-1); transition:color .2s; }}
    .nav-item:hover, .nav-item.active {{ color:var(--bordeaux); }}
    .nav-logo {{ font-family:'Cormorant Garamond',serif; font-size:26px; font-weight:400; letter-spacing:.25em; text-align:center; line-height:1; }}
    .nav-logo .accent {{ display:block; font-family:'JetBrains Mono',monospace; font-size:8px; letter-spacing:.2em; color:var(--bordeaux); margin-top:4px; text-transform:uppercase; }}
    .nav-icon {{ cursor:pointer; color:var(--gray-1); font-size:18px; }}

    .container {{ max-width:1400px; margin:0 auto; padding:0 48px; }}
    .eyebrow {{ font-family:'JetBrains Mono',monospace; font-size:10px; letter-spacing:.25em; text-transform:uppercase; color:var(--bordeaux); }}

    /* HERO */
    .hero-compact {{ background:var(--bone); padding:80px 0 60px; border-bottom:1px solid var(--line); }}
    .hero-headline {{ font-family:'Cormorant Garamond',serif; font-size:72px; font-weight:300; color:var(--ink); line-height:1; margin-top:20px; }}
    .hero-subhead {{ font-family:'Cormorant Garamond',serif; font-style:italic; font-size:24px; color:var(--gray-2); margin-top:16px; }}
    .hero-meta {{ font-family:'JetBrains Mono',monospace; font-size:10px; color:var(--gray-3); letter-spacing:.2em; text-transform:uppercase; margin-top:24px; }}

    /* FILTER */
    .filter-bar {{ background:var(--white); border-bottom:1px solid var(--line); padding:20px 48px; display:flex; align-items:center; gap:16px; flex-wrap:wrap; }}
    .filter-label {{ font-family:'JetBrains Mono',monospace; font-size:10px; letter-spacing:.2em; text-transform:uppercase; color:var(--gray-3); }}
    .filter-btn {{ font-family:'JetBrains Mono',monospace; font-size:10px; letter-spacing:.15em; text-transform:uppercase; color:var(--gray-1); padding:6px 16px; border:1px solid var(--line); cursor:pointer; transition:all .2s; background:transparent; }}
    .filter-btn:hover, .filter-btn.active {{ border-color:var(--bordeaux); color:var(--bordeaux); }}

    /* PRODUCTS */
    .products-section {{ padding:80px 0 120px; }}
    .products-header {{ display:flex; justify-content:space-between; align-items:center; margin-bottom:48px; }}
    .products-title {{ font-family:'Cormorant Garamond',serif; font-size:44px; font-weight:300; color:var(--ink); }}
    .products-count {{ font-family:'JetBrains Mono',monospace; font-size:10px; color:var(--gray-3); letter-spacing:.15em; }}
    .product-grid {{ display:grid; grid-template-columns:repeat(4,1fr); gap:32px; }}
    .product-card {{ display:block; transition:transform .3s; }}
    .product-card:hover {{ transform:translateY(-4px); }}
    .product-card.hidden {{ display:none; }}
    .product-img-wrap {{ aspect-ratio:3/4; overflow:hidden; background:var(--bone); }}
    .product-img-wrap img {{ width:100%; height:100%; object-fit:cover; transition:transform .6s ease; }}
    .product-card:hover .product-img-wrap img {{ transform:scale(1.04); }}
    .product-info {{ padding:20px 0; }}
    .product-code {{ font-family:'JetBrains Mono',monospace; font-size:10px; color:var(--bordeaux); letter-spacing:.12em; }}
    .product-name {{ font-family:'Cormorant Garamond',serif; font-size:22px; font-weight:400; color:var(--ink); margin-top:6px; line-height:1.2; }}
    .product-material {{ font-family:'Inter',sans-serif; font-size:11px; color:var(--gray-2); margin-top:4px; }}
    .product-action {{ display:flex; align-items:center; justify-content:space-between; margin-top:16px; padding-top:16px; border-top:1px solid var(--line); }}
    .product-cta {{ font-family:'JetBrains Mono',monospace; font-size:10px; letter-spacing:.15em; text-transform:uppercase; color:var(--bordeaux); border-bottom:1px solid var(--bordeaux); padding-bottom:1px; }}
    .product-wishlist {{ font-size:18px; color:var(--gray-3); cursor:pointer; transition:color .2s; }}
    .product-wishlist:hover {{ color:var(--bordeaux); }}

    /* CTA */
    .cta-section {{ background:var(--bordeaux); padding:80px 48px; text-align:center; }}
    .cta-title {{ font-family:'Cormorant Garamond',serif; font-size:52px; font-weight:300; color:var(--white); line-height:1.1; margin-bottom:16px; }}
    .cta-sub {{ font-family:'Inter',sans-serif; font-size:13px; color:rgba(255,255,255,.7); letter-spacing:.15em; text-transform:uppercase; margin-bottom:40px; }}
    .btn-white {{ display:inline-block; padding:16px 40px; background:var(--white); color:var(--bordeaux); border:1px solid var(--white); font-family:'Inter',sans-serif; font-size:11px; font-weight:500; letter-spacing:.2em; text-transform:uppercase; transition:background .25s,color .25s; }}
    .btn-white:hover {{ background:transparent; color:var(--white); }}
    .btn-outline-white {{ display:inline-block; padding:16px 40px; background:transparent; color:var(--white); border:1px solid rgba(255,255,255,.5); font-family:'Inter',sans-serif; font-size:11px; font-weight:500; letter-spacing:.2em; text-transform:uppercase; margin-left:16px; transition:border-color .25s; }}
    .btn-outline-white:hover {{ border-color:var(--white); }}

    /* FOOTER */
    .footer {{ background:var(--paper); color:var(--gray-1); padding:80px 48px 40px; border-top:1px solid var(--line); }}
    .footer-grid {{ display:grid; grid-template-columns:2fr 1fr 1fr 1fr 1fr; gap:48px; padding-bottom:60px; border-bottom:1px solid var(--line); max-width:1400px; margin:0 auto; }}
    .footer-brand h3 {{ font-family:'Cormorant Garamond',serif; font-size:28px; font-weight:300; letter-spacing:.2em; margin-bottom:16px; color:var(--ink); }}
    .footer-brand p {{ font-size:12px; color:var(--gray-2); line-height:1.7; max-width:320px; }}
    .footer-social {{ margin-top:24px; display:flex; gap:12px; }}
    .footer-social a {{ border:1px solid var(--line); width:36px; height:36px; display:flex; align-items:center; justify-content:center; color:var(--gray-2); transition:color .3s,border-color .3s; }}
    .footer-social a:hover {{ color:var(--bordeaux); border-color:var(--bordeaux); }}
    .footer-col h4 {{ font-family:'JetBrains Mono',monospace; font-size:10px; letter-spacing:.25em; text-transform:uppercase; color:var(--bordeaux); margin-bottom:20px; }}
    .footer-col li {{ font-size:12px; color:var(--gray-1); margin-bottom:10px; transition:color .2s; }}
    .footer-col li:hover {{ color:var(--bordeaux); }}
    .footer-col a {{ color:inherit; }}
    .footer-bottom {{ display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:9px; color:var(--gray-3); letter-spacing:.15em; max-width:1400px; margin:32px auto 0; }}

    @media (max-width:768px) {{
      .utility-bar {{ padding:8px 24px; font-size:9px; }}
      .utility-bar span:first-child {{ display:none; }}
      .main-nav {{ padding:0 24px; height:60px; }}
      .nav-left, .nav-right {{ display:none; }}
      .hero-compact {{ padding:60px 0 40px; }}
      .hero-headline {{ font-size:48px; }}
      .container {{ padding:0 24px; }}
      .filter-bar {{ padding:16px 24px; overflow-x:auto; flex-wrap:nowrap; }}
      .product-grid {{ grid-template-columns:repeat(2,1fr); gap:20px; }}
      .products-title {{ font-size:32px; }}
      .cta-section {{ padding:60px 24px; }}
      .cta-title {{ font-size:36px; }}
      .btn-outline-white {{ display:block; margin-left:0; margin-top:12px; }}
      .footer {{ padding:60px 24px 32px; }}
      .footer-grid {{ grid-template-columns:1fr 1fr; gap:32px; }}
      .footer-brand {{ grid-column:1/-1; }}
      .footer-bottom {{ flex-direction:column; gap:12px; text-align:center; }}
    }}
  </style>
</head>
<body>

<div class="utility-bar">
  <span>NEW COLLECTION FW 2025 — INTERAMENTE MADE IN ITALY</span>
  <a href="prenota.html">Prenota una visita &rarr;</a>
  <span>IT / EN</span>
</div>

<nav class="main-nav">
  <div class="nav-left">
    <a href="about.html" class="nav-item">Azienda</a>
    <a href="fabio-gavazzi.html" class="nav-item">Brand</a>
    <a href="collezioni-donna.html" class="nav-item active">Collezioni</a>
  </div>
  <a href="index.html" class="nav-logo">
    FURECO
    <span class="accent">FUR ENTERPRISE COMPANY · DAL 1924</span>
  </a>
  <div class="nav-right">
    <a href="servizi.html" class="nav-item">Servizi</a>
    <a href="showroom.html" class="nav-item">Showroom</a>
    <a href="sostenibilita.html" class="nav-item">Sostenibilit&agrave;</a>
    <span class="nav-icon">&#9906;</span>
  </div>
</nav>

<section class="hero-compact">
  <div class="container">
    <p class="eyebrow">— FABIO GAVAZZI · COLLEZIONE DONNA</p>
    <h1 class="hero-headline">Collezione<br/>Donna FW 2025</h1>
    <p class="hero-subhead">Cincill&agrave;, visone, zibellino, shearling e cashmere Loro Piana</p>
    <p class="hero-meta">Fabio Gavazzi &middot; Milano &middot; Made in Italy &middot; Dal 1924 &middot; {total} capi</p>
  </div>
</section>

<div class="filter-bar">
  <span class="filter-label">Filtra:</span>
  {filters_html}
</div>

<section class="products-section">
  <div class="container">
    <div class="products-header">
      <h2 class="products-title">Tutti i capi</h2>
      <span class="products-count" id="count">{total} CAPI · FW 2025</span>
    </div>
    <div class="product-grid" id="grid">
{cards_html}
    </div>
  </div>
</section>

<section class="cta-section">
  <h2 class="cta-title">Vivi la collezione<br/>in atelier</h2>
  <p class="cta-sub">Visite private su appuntamento &middot; Milano Montenapoleone &amp; Seregno</p>
  <a class="btn-white" href="prenota.html">Prenota una Visita Privata</a>
  <a class="btn-outline-white" href="collezioni-uomo.html">Scopri la Collezione Uomo</a>
</section>

<footer class="footer">
  <div class="footer-grid">
    <div class="footer-brand">
      <h3>FURECO<br/><em style="font-style:italic;font-size:14px;color:var(--gray-2);">Fur Enterprise Co.</em></h3>
      <p>Pellicceria italiana dal 1924. Quattro generazioni di artigianato, ricerca e innovazione al servizio del lusso senza tempo.</p>
      <div class="footer-social">
        <a href="https://www.instagram.com/fabiogavazziofficial" target="_blank" aria-label="Instagram">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
        </a>
      </div>
    </div>
    <div class="footer-col"><h4>Brand</h4><ul>
      <li><a href="fabio-gavazzi.html">Fabio Gavazzi</a></li>
      <li><a href="fabio-gavazzi-man.html">Fabio Gavazzi Man</a></li>
      <li><a href="mavina.html">Mavina</a></li>
      <li><a href="fureco-home.html">Fureco Home</a></li>
    </ul></div>
    <div class="footer-col"><h4>Azienda</h4><ul>
      <li><a href="about.html">Chi Siamo</a></li>
      <li><a href="fureco-world.html">Mondo Fureco</a></li>
      <li><a href="sostenibilita.html">Sostenibilit&agrave;</a></li>
    </ul></div>
    <div class="footer-col"><h4>Servizi</h4><ul>
      <li><a href="servizi.html">Bespoke</a></li>
      <li><a href="servizi.html">Made to Measure</a></li>
      <li><a href="servizi.html">Fur Restyling</a></li>
      <li><a href="servizi.html">Cura &amp; Conservazione</a></li>
    </ul></div>
    <div class="footer-col"><h4>Showroom</h4><ul>
      <li><a href="showroom-montenapoleone.html">Milano &middot; Montenapoleone</a></li>
      <li><a href="showroom-seregno.html">Seregno (MB)</a></li>
      <li><a href="prenota.html">Prenota Visita</a></li>
    </ul></div>
  </div>
  <div class="footer-bottom">
    <span>&copy; 2026 Fureco Srl &middot; P.IVA IT00794320960</span>
    <span>Privacy &middot; Cookie &middot; Shipping &middot; Recesso</span>
  </div>
</footer>

<script>
  const btns = document.querySelectorAll('.filter-btn');
  const cards = document.querySelectorAll('.product-card');
  const countEl = document.getElementById('count');

  btns.forEach(btn => {{
    btn.addEventListener('click', function() {{
      btns.forEach(b => b.classList.remove('active'));
      this.classList.add('active');
      const filter = this.dataset.filter;
      let visible = 0;
      cards.forEach(card => {{
        const match = filter === 'all' || card.dataset.cat === filter;
        card.classList.toggle('hidden', !match);
        if (match) visible++;
      }});
      countEl.textContent = visible + ' CAPI · FW 2025';
    }});
  }});
</script>
</body>
</html>'''

out = os.path.join(SITE, 'collezioni-donna.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Scritto: {out}')
print(f'Totale prodotti: {total}')
