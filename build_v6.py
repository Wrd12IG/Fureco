import re

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v4-MEDIA.html', 'r', encoding='utf-8') as f:
    v4 = f.read()

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v5-VIDEO-FULL.html', 'r', encoding='utf-8') as f:
    v5 = f.read()

# From V5, we want:
# 1. The full HTML from <section class="hero-split"> down to the end of <!-- SEZIONE 02 — COLLEZIONI -->
hero_start_v5 = v5.find('<!-- SEZIONE 01 — HERO -->')
if hero_start_v5 == -1: hero_start_v5 = v5.find('<section class="hero-split">')
coll_end_v5 = v5.find('<!-- SEZIONE 03 — HERITAGE -->')

v5_hero_coll = v5[hero_start_v5:coll_end_v5]

# From V5, we need the specific CSS added for the hero full width and grid.
# The differences in CSS are mostly the media queries or the specific new classes.
# Actually, V5 already HAS all the V4 CSS up to the point it was forked, but V5 misses the bordeaux top bar and some cleanups.
# So if we take V5 as the base...
# Let's take V5 as the base.
# Then we replace the top bar in V5 with the top bar from V4.
v4_utility = re.search(r'<div class="utility-bar">.*?</div>', v4, re.DOTALL)
v5 = re.sub(r'<div class="utility-bar">.*?</div>', v4_utility.group(0), v5, flags=re.DOTALL)

# Then we replace the Sections 03 to 06 in V5 with the Sections 03 to end (before footer) from V4
v4_sections_start = v4.find('<!-- SEZIONE 03 — HERITAGE -->')
v4_sections_end = v4.find('<!-- FOOTER -->')

v5_sections_start = v5.find('<!-- SEZIONE 03 — HERITAGE -->')
v5_sections_end = v5.find('<!-- FOOTER -->')

v5 = v5[:v5_sections_start] + v4[v4_sections_start:v4_sections_end] + v5[v5_sections_end:]

# We also need to copy the CSS for utility-bar from V4 to V5, because V4 changed it to bordeaux.
# In V4:
#   .utility-bar {
#    background: var(--bordeaux);
#    color: var(--white);
#    ...
#    font-family: 'Cormorant Garamond', serif;
#    text-transform: none;
#    font-size: 14px;
#    font-style: italic;
v4_utility_css = re.search(r'\.utility-bar \{.*?\.utility-bar a:hover \{.*?\}', v4, re.DOTALL)
if v4_utility_css:
    v5 = re.sub(r'\.utility-bar \{.*?\.utility-bar a:hover \{.*?\}', v4_utility_css.group(0), v5, flags=re.DOTALL)

# Let's rename the title
v5 = v5.replace('<title>Wireframe v5 Video Full — Fureco × Fabio Gavazzi</title>', '<title>Wireframe v6 FINAL — Fureco × Fabio Gavazzi</title>')

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v6-FINAL.html', 'w', encoding='utf-8') as f:
    f.write(v5)

print("V6 built successfully.")
