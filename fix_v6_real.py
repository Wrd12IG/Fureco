with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v4-MEDIA.html', 'r', encoding='utf-8') as f:
    v4 = f.read()

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v5-VIDEO-FULL.html', 'r', encoding='utf-8') as f:
    v5 = f.read()

import re

# 1. HTML Replace
v4_hero_start = v4.find('<!-- ============================================================')
v4_coll_end = v4.find('<!-- SEZIONE 03 — HERITAGE -->')

v5_hero_start = v5.find('<!-- ============================================================')
v5_coll_end = v5.find('<!-- SEZIONE 03 — HERITAGE -->')

v6 = v4[:v4_hero_start] + v5[v5_hero_start:v5_coll_end] + v4[v4_coll_end:]

# 2. Desktop CSS Replace
v4_css_start = v6.find('/* ==================== HERO 50/50 SPLIT')
v4_css_end = v6.find('/* ============================================================', v4_css_start)

v5_css_start = v5.find('/* ==================== VIDEO FULL WIDTH')
v5_css_end = v5.find('/* ==================== MOBILE')

v6 = v6[:v4_css_start] + v5[v5_css_start:v5_css_end] + "\n  " + v6[v4_css_end:]

# 3. Mobile CSS Replace
v4_mob_start = v6.find('/* --- HERO SPLIT --- */')
v4_mob_end = v6.find('/* --- SECTIONS GENERAL --- */')

v5_mob_start = v5.find('/* --- HERO FULL VIDEO --- */')
v5_mob_end = v5.find('/* --- SECTIONS GENERAL --- */')

v6 = v6[:v4_mob_start] + v5[v5_mob_start:v5_mob_end] + "\n    " + v6[v4_mob_end:]

# Set title
v6 = v6.replace('<title>Wireframe v4 Media — Fureco × Fabio Gavazzi</title>', '<title>Wireframe v6 FINAL — Fureco × Fabio Gavazzi</title>')

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v6-FINAL.html', 'w', encoding='utf-8') as f:
    f.write(v6)
print("Done!")
