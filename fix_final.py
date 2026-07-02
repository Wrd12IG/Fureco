with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v4-MEDIA.html', 'r', encoding='utf-8') as f:
    v4 = f.read()

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v5-VIDEO-FULL.html', 'r', encoding='utf-8') as f:
    v5 = f.read()

import re

# HTML replacement
v4_html_start = v4.find('<!-- ============================================================')
# we need to find the SECOND occurrence, wait. 
# The first occurrence might be something else. Let's use regex to be safe.
v4_html_match = re.search(r'<!-- ============================================================\s*HERO.*?<!-- SEZIONE 03 — HERITAGE -->', v4, re.DOTALL)
v5_html_match = re.search(r'<!-- ============================================================\s*HERO.*?<!-- SEZIONE 03 — HERITAGE -->', v5, re.DOTALL)

if v4_html_match and v5_html_match:
    v6 = v4.replace(v4_html_match.group(0), v5_html_match.group(0))
else:
    print("HTML match failed")
    exit(1)

# Desktop CSS Replacement
v4_css_match = re.search(r'/\* ==================== HERO 50/50 SPLIT.*?/\* ============================================================\s*SECTIONS \(after hero\)', v6, re.DOTALL)
v5_css_match = re.search(r'/\* ==================== VIDEO FULL WIDTH.*?/\* ==================== MOBILE ==================== \*/', v5, re.DOTALL)

if v4_css_match and v5_css_match:
    v6 = v6.replace(v4_css_match.group(0), v5_css_match.group(0).replace('/* ==================== MOBILE ==================== */', '/* ============================================================\n     SECTIONS (after hero)\n     ============================================================ */'))
else:
    print("Desktop CSS match failed")
    print(bool(v4_css_match), bool(v5_css_match))
    exit(1)

# Mobile CSS Replacement
v4_mob_match = re.search(r'/\* --- HERO SPLIT --- \*/.*?/\* --- SECTIONS GENERAL --- \*/', v6, re.DOTALL)
v5_mob_match = re.search(r'/\* --- HERO FULL VIDEO --- \*/.*?/\* --- SECTIONS GENERAL --- \*/', v5, re.DOTALL)

if v4_mob_match and v5_mob_match:
    v6 = v6.replace(v4_mob_match.group(0), v5_mob_match.group(0))
else:
    print("Mobile CSS match failed")
    print(bool(v4_mob_match), bool(v5_mob_match))
    exit(1)

v6 = v6.replace('<title>Wireframe v4 Media — Fureco × Fabio Gavazzi</title>', '<title>Wireframe v6 FINAL — Fureco × Fabio Gavazzi</title>')

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v6-FINAL.html', 'w', encoding='utf-8') as f:
    f.write(v6)

print("V6 constructed flawlessly!")
