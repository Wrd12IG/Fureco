import re
with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v5-VIDEO-FULL.html', 'r', encoding='utf-8') as f:
    v5 = f.read()

v5_css_start = v5.find('/* ==================== VIDEO FULL WIDTH ==================== */')
v5_css_end = v5.find('/* ==================== MOBILE ==================== */')
print(v5[v5_css_start:v5_css_end])
