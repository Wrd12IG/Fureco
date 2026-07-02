import re

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v4-MEDIA.html', 'r', encoding='utf-8') as f:
    content = f.read()

def extract_section(name):
    # Matches from <!-- SEZIONE ... name --> until just before the next <!-- SEZIONE
    # or the end container div
    pattern = re.compile(r'(<!-- SEZIONE \d+ — ' + name + r' -->.*?)(?=<!-- SEZIONE|</div>\s*<!-- ==================== FOOTER ==================== -->)', re.DOTALL)
    match = pattern.search(content)
    if match:
        return match.group(1)
    return None

sec_showroom = extract_section('SHOWROOM')
sec_shop = extract_section('SHOP ONLINE')
sec_recensioni = extract_section('RECENSIONI')
sec_servizi = extract_section('SERVIZI')
sec_furmark = extract_section('FURMARK')

if sec_showroom and sec_shop and sec_recensioni and sec_servizi and sec_furmark:
    new_sections = "".join([sec_showroom, sec_servizi, sec_furmark, sec_shop, sec_recensioni])
    
    # We replace from <!-- SEZIONE 04 — SHOWROOM --> up to before footer
    pattern_all = re.compile(r'<!-- SEZIONE \d+ — SHOWROOM -->.*?(?=</div>\s*<!-- ==================== FOOTER ==================== -->)', re.DOTALL)
    
    content = pattern_all.sub(new_sections, content)

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v4-MEDIA.html', 'w', encoding='utf-8') as f:
    f.write(content)
