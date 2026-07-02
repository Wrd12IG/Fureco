with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v5-VIDEO-FULL.html', 'r', encoding='utf-8') as f:
    v5 = f.read()
start = v5.find('<section class="hero-split"')
end = v5.find('<div style="width:100%; max-width: 1200px;')
print(v5[start:end])
