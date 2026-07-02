with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v4-MEDIA.html', 'r', encoding='utf-8') as f:
    v4 = f.read()
    
# Extract SEZIONE 02 from V4
start_sez2 = v4.find('<!-- SEZIONE 02 — COLLEZIONI -->')
end_sez2 = v4.find('<!-- SEZIONE 03 — HERITAGE -->')
sez2_html = v4[start_sez2:end_sez2]

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v6-FINAL.html', 'r', encoding='utf-8') as f:
    v6 = f.read()

# Make brand tiles square by modifying their CSS
# I will append aspect-ratio to the specific brand-tile override from V5
v6 = v6.replace(
    '.brand-tile {\n    justify-content: flex-end !important;\n    padding-bottom: 40px !important;\n  }',
    '.brand-tile {\n    justify-content: flex-end !important;\n    padding-bottom: 40px !important;\n    aspect-ratio: 1 / 1;\n  }'
)

# Insert SEZIONE 02 into V6
v6 = v6.replace('<!-- SEZIONE 03 — HERITAGE -->', sez2_html + '<!-- SEZIONE 03 — HERITAGE -->')

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v6-FINAL.html', 'w', encoding='utf-8') as f:
    f.write(v6)

print("V6 fixed!")
