with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v4-MEDIA.html', 'r', encoding='utf-8') as f:
    v4 = f.read()
print("v4 html start:", v4.find('<!-- ============================================================\n     HERO 50/50'))
print("v4 html start fallback:", v4.find('<section class="hero-split"'))
