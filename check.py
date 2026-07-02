with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v4-MEDIA.html', 'r', encoding='utf-8') as f:
    v4 = f.read()

v4_hero_css_start = v4.find('/* ==================== HERO ==================== */')
v4_hero_css_end = v4.find('/* ==================== SECTIONS (after hero)')

print(v4[v4_hero_css_start:v4_hero_css_start+500])
print("==============================")
print(v4[v4_hero_css_end-500:v4_hero_css_end])
