with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v4-MEDIA.html', 'r', encoding='utf-8') as f:
    v4 = f.read()
print("v4 css start:", v4.find('/* ============================================================\n     HERO 50/50 SPLIT'))
print("v4 css end:", v4.find('/* ============================================================\n     SECTIONS (after hero)'))
