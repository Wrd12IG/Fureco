with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v4-MEDIA.html', 'r', encoding='utf-8') as f:
    v4 = f.readlines()

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v5-VIDEO-FULL.html', 'r', encoding='utf-8') as f:
    v5 = f.readlines()

# Convert 1-based indices to 0-based slice indices
# CSS Desktop
# v4: 128 to 374 -> index 127 to 374
# v5: 1152 to 1197 -> index 1151 to 1197
v5_css_desktop = v5[1151:1197]
v4_part1 = v4[:127]
v4_part2 = v4[374:1194]

# CSS Mobile
# v4: 1195 to 1229 -> index 1194 to 1229
# v5: 1223 to 1261 -> index 1222 to 1261
v5_css_mobile = v5[1222:1261]
v4_part3 = v4[1229:1410]

# HTML
# v4: 1411 to 1589 -> index 1410 to 1589
# v5: 1411 to 1512 -> index 1410 to 1512
v5_html = v5[1410:1512]
v4_part4 = v4[1589:]

v6_lines = v4_part1 + v5_css_desktop + v4_part2 + v5_css_mobile + v4_part3 + v5_html + v4_part4

v6_str = "".join(v6_lines)
v6_str = v6_str.replace('<title>Wireframe v4 Media — Fureco × Fabio Gavazzi</title>', '<title>Wireframe v6 FINAL — Fureco × Fabio Gavazzi</title>')

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v6-FINAL.html', 'w', encoding='utf-8') as f:
    f.write(v6_str)

print("V6 assembled using exact line numbers.")
