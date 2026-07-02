import re

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v4-MEDIA.html', 'r', encoding='utf-8') as f:
    v4 = f.read()

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v5-VIDEO-FULL.html', 'r', encoding='utf-8') as f:
    v5 = f.read()

# EXTRACT V5 HTML
v5_html_start = v5.find('<!-- ============================================================')
if v5_html_start == -1: v5_html_start = v5.find('<section class="hero-split"')
v5_coll_end = v5.find('<!-- SEZIONE 03 — HERITAGE -->')
v5_html = v5[v5_html_start:v5_coll_end]

# REPLACE IN V4 HTML
v4_html_start = v4.find('<!-- ============================================================')
if v4_html_start == -1: v4_html_start = v4.find('<section class="hero-split"')
v4_coll_end = v4.find('<!-- SEZIONE 03 — HERITAGE -->')

v6 = v4[:v4_html_start] + v5_html + v4[v4_coll_end:]

# EXTRACT V5 CSS (Desktop)
v5_css_start = v5.find('/* ==================== VIDEO FULL WIDTH ==================== */')
v5_css_end = v5.find('/* ==================== MOBILE ==================== */')
v5_css = v5[v5_css_start:v5_css_end] if v5_css_start != -1 else ""

# EXTRACT V5 CSS (Mobile)
v5_mob_start = v5.find('/* --- HERO FULL VIDEO --- */')
v5_mob_end = v5.find('/* --- SECTIONS GENERAL --- */')
v5_mob_css = v5[v5_mob_start:v5_mob_end] if v5_mob_start != -1 else ""

# APPEND V5 CSS inside V6
# Insert Desktop CSS right before /* ==================== MOBILE ==================== */
mob_marker = v6.find('/* ==================== MOBILE ==================== */')
if mob_marker != -1:
    v6 = v6[:mob_marker] + v5_css + "\n  " + v6[mob_marker:]

# Insert Mobile CSS right before /* --- SECTIONS GENERAL --- */
mob_sec_marker = v6.find('/* --- SECTIONS GENERAL --- */')
if mob_sec_marker != -1:
    v6 = v6[:mob_sec_marker] + v5_mob_css + "\n    " + v6[mob_sec_marker:]

# Fix the V5 opacity to what they liked
v6 = v6.replace(
    '.brand-tile-image-bg-real { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; opacity:0; transition:opacity .6s ease; z-index:0; }',
    '.brand-tile-image-bg-real { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; opacity:0.4; filter: contrast(0.9) grayscale(20%); transition:all .6s ease; z-index:0; }'
)
v6 = v6.replace(
    '.brand-tile:hover .brand-tile-image-bg-real { opacity:.18; }',
    '.brand-tile:hover .brand-tile-image-bg-real { opacity:0.65; filter: contrast(1.15) grayscale(0%); transform: scale(1.03); }'
)

# Rename title
v6 = v6.replace('<title>Wireframe v4 Media — Fureco × Fabio Gavazzi</title>', '<title>Wireframe v6 FINAL — Fureco × Fabio Gavazzi</title>')

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v6-FINAL.html', 'w', encoding='utf-8') as f:
    f.write(v6)

print("V6 built safely by appending CSS!")
