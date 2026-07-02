import re

# We will use v4 as the base because it has all the correct layout CSS for the bottom sections.
with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v4-MEDIA.html', 'r', encoding='utf-8') as f:
    v4 = f.read()

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v5-VIDEO-FULL.html', 'r', encoding='utf-8') as f:
    v5 = f.read()

# EXTRACT V5 HERO + COLLEZIONI HTML
v5_hero_start = v5.find('<!-- ============================================================')
if v5_hero_start == -1: v5_hero_start = v5.find('<section class="hero-split"')
v5_coll_end = v5.find('<!-- SEZIONE 03 — HERITAGE -->')
v5_html = v5[v5_hero_start:v5_coll_end]

# REPLACE V4 HERO + COLLEZIONI HTML
v4_hero_start = v4.find('<!-- ============================================================')
if v4_hero_start == -1: v4_hero_start = v4.find('<section class="hero-split"')
v4_coll_end = v4.find('<!-- SEZIONE 03 — HERITAGE -->')

v6 = v4[:v4_hero_start] + v5_html + v4[v4_coll_end:]

# EXTRACT V5 CSS for hero-video-full and brand-tile grid (and related overwrites)
# Let's just grab the whole block of CSS from V5 between /* ==================== VIDEO FULL WIDTH ==================== */ and /* ==================== MOBILE ==================== */
v5_css_start = v5.find('/* ==================== VIDEO FULL WIDTH ==================== */')
v5_css_end = v5.find('/* ==================== MOBILE ==================== */')
if v5_css_start != -1 and v5_css_end != -1:
    v5_css = v5[v5_css_start:v5_css_end]
else:
    v5_css = ""

# Also we need to make sure the mobile CSS for hero/brands is updated. 
# V5 mobile CSS for hero/brands starts at /* --- HERO FULL VIDEO --- */ and ends at /* --- SECTIONS GENERAL --- */
v5_mob_start = v5.find('/* --- HERO FULL VIDEO --- */')
v5_mob_end = v5.find('/* --- SECTIONS GENERAL --- */')
if v5_mob_start != -1 and v5_mob_end != -1:
    v5_mob_css = v5[v5_mob_start:v5_mob_end]
else:
    v5_mob_css = ""

# In V6 (which currently has V4's CSS), replace the hero CSS and collezioni CSS.
# In V4, the hero CSS was mostly in /* ==================== HERO ==================== */
# The Collezioni CSS was in /* ==================== COLLEZIONI SPLIT ==================== */ and /* --- COLLEZIONI SPLIT --- */ (mobile)
# Let's replace the HERO css block in V4
v4_hero_css_start = v6.find('/* ==================== HERO ==================== */')
v4_hero_css_end = v6.find('/* ==================== SECTIONS (after hero)')
if v4_hero_css_start != -1 and v4_hero_css_end != -1:
    v6 = v6[:v4_hero_css_start] + v5_css + "\n" + v6[v4_hero_css_end:]

# Replace the mobile HERO and COLLEZIONI in V4
v4_mob_hero_start = v6.find('/* --- HERO --- */')
v4_mob_hero_end = v6.find('/* --- SECTIONS GENERAL --- */')
if v4_mob_hero_start != -1 and v4_mob_hero_end != -1:
    v6 = v6[:v4_mob_hero_start] + v5_mob_css + "\n" + v6[v4_mob_hero_end:]

# Update the title
v6 = v6.replace('<title>Wireframe v4 Media — Fureco × Fabio Gavazzi</title>', '<title>Wireframe v6 FINAL — Fureco × Fabio Gavazzi</title>')

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v6-FINAL.html', 'w', encoding='utf-8') as f:
    f.write(v6)

print("V6 fixed successfully.")
