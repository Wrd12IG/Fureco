import re

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v5-VIDEO-FULL.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract .hero-brands
# Start string: <div class="hero-brands">
# End string: <div class="hero-media"> or </section>
# Wait, hero-brands is the last element in hero-split section.
m_brands = re.search(r'(<div class="hero-brands">.*?)(\s*</section>)', content, re.DOTALL)
if m_brands:
    hero_brands = m_brands.group(1)
    # Remove hero-brands from hero-split
    content = content.replace(hero_brands, '')

# 2. Extract hero-media overlay and remove hero-media
m_overlay = re.search(r'(<div class="hero-media-overlay">.*?</div>)', content, re.DOTALL)
if m_overlay:
    hero_overlay = m_overlay.group(1)
    
    # Remove hero-media completely
    m_media = re.search(r'<div class="hero-media">.*?</div>\s*</div>', content, re.DOTALL)
    if m_media:
        # Actually hero-media has nested divs, let's just use replace with regex
        content = re.sub(r'<div class="hero-media">.*?(?=\s*</section>)', '', content, flags=re.DOTALL)

    # Insert hero_overlay after hero-video-full
    # So the hero section has hero-video-full and then hero-overlay.
    # To center it, let's wrap it or modify hero-split.
    # We will just append the overlay right before </section>
    content = re.sub(r'(</section>)', hero_overlay + r'\n\1', content, count=1)

# 3. Modify hero-split to be centered flex
content = content.replace('<section class="hero-split ">', 
    '<section class="hero-split" style="display: flex; align-items: center; justify-content: center; position: relative; width: 100%; border: none;">')

# Also modify hero-media-overlay to be centered and not absolute at bottom left
content = content.replace('<div class="hero-media-overlay">', 
    '<div class="hero-media-overlay" style="position: relative; z-index: 2; text-align: center; padding: 0 40px; margin: auto; display: flex; flex-direction: column; align-items: center; justify-content: center; left: auto; right: auto; bottom: auto; top: auto; transform: none; width: 100%; height: 100%;">')

# 4. Replace Collezioni sliders with the extracted hero_brands
# Find <div class="collezioni-split">...</div> and replace it with hero_brands
# Collezioni section ends at the next <!-- SEZIONE
m_coll = re.search(r'(<div class="collezioni-split">.*?)(?=<!-- SEZIONE 03)', content, re.DOTALL)
if m_coll and m_brands:
    collezioni_split = m_coll.group(1)
    # Let's clean up hero_brands to fit as a normal grid (remove absolute positioning if any, though it relies on CSS which we can keep)
    # The CSS for hero-brands is grid-template-columns: 1fr 1fr;
    # It might need a max-width and margin auto.
    hero_brands_adjusted = hero_brands.replace('<div class="hero-brands">', '<div class="hero-brands" style="max-width: 1200px; margin: 0 auto; width: 100%;">')
    content = content.replace(collezioni_split, hero_brands_adjusted + '\n  ')

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v5-VIDEO-FULL.html', 'w', encoding='utf-8') as f:
    f.write(content)

