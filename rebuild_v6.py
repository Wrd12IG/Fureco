import re

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v4-MEDIA.html', 'r', encoding='utf-8') as f:
    v4 = f.read()

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v5-VIDEO-FULL.html', 'r', encoding='utf-8') as f:
    v5 = f.read()

# 1. EXTRACT V5 HERO + COLLEZIONI HTML
v5_hero_start = v5.find('<!-- ============================================================')
if v5_hero_start == -1: v5_hero_start = v5.find('<section class="hero-split"')
v5_coll_end = v5.find('<!-- SEZIONE 03 — HERITAGE -->')
v5_html = v5[v5_hero_start:v5_coll_end]

# 2. EXTRACT V4 BASE HTML
v4_hero_start = v4.find('<!-- ============================================================')
if v4_hero_start == -1: v4_hero_start = v4.find('<section class="hero-split"')
v4_coll_end = v4.find('<!-- SEZIONE 03 — HERITAGE -->')

v6_html_body = v4[:v4_hero_start] + v5_html + v4[v4_coll_end:]

# 3. NOW FOR THE CSS
# In v5, the relevant new CSS for hero/collezioni is bounded by:
# /* ==================== VIDEO FULL WIDTH ==================== */
# down to /* ==================== MOBILE ==================== */ (for desktop)
v5_css_start = v5.find('/* ==================== VIDEO FULL WIDTH ==================== */')
v5_css_end = v5.find('/* ==================== MOBILE ==================== */')
v5_css_desktop = v5[v5_css_start:v5_css_end] if v5_css_start != -1 else ""

# And for mobile:
# /* --- HERO FULL VIDEO --- */
# down to /* --- SECTIONS GENERAL --- */
v5_mob_start = v5.find('/* --- HERO FULL VIDEO --- */')
v5_mob_end = v5.find('/* --- SECTIONS GENERAL --- */')
v5_css_mobile = v5[v5_mob_start:v5_mob_end] if v5_mob_start != -1 else ""

# In V4, we need to replace the HERO and COLLEZIONI css with these blocks.
# Desktop CSS to replace in V4:
# from /* ==================== HERO 50/50 ==================== */
# to /* ============================================================
#      SECTIONS (after hero)
v4_css_start = v6_html_body.find('/* ==================== HERO 50/50 ==================== */')
v4_css_end = v6_html_body.find('/* ============================================================', v4_css_start+10)
if v4_css_start != -1 and v4_css_end != -1:
    v6_html_body = v6_html_body[:v4_css_start] + v5_css_desktop + "\n" + v6_html_body[v4_css_end:]

# Mobile CSS to replace in V4:
# from /* --- HERO --- */
# to /* --- SECTIONS GENERAL --- */
v4_mob_start = v6_html_body.find('/* --- HERO --- */')
v4_mob_end = v6_html_body.find('/* --- SECTIONS GENERAL --- */')
if v4_mob_start != -1 and v4_mob_end != -1:
    v6_html_body = v6_html_body[:v4_mob_start] + v5_css_mobile + "\n" + v6_html_body[v4_mob_end:]

# Update the title
v6_html_body = v6_html_body.replace('<title>Wireframe v4 Media — Fureco × Fabio Gavazzi</title>', '<title>Wireframe v6 FINAL — Fureco × Fabio Gavazzi</title>')

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v6-FINAL.html', 'w', encoding='utf-8') as f:
    f.write(v6_html_body)

print("V6 rebuilt.")
