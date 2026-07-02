import re

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v5-VIDEO-FULL.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the first definition (lines ~1099)
content = re.sub(
    r'\.brand-tile-image-bg-real\s*\{\s*position:absolute;\s*inset:0;\s*width:100%;\s*height:100%;\s*object-fit:cover;\s*opacity:0;\s*transition:opacity \.6s ease;\s*z-index:0;\s*\}',
    r'.brand-tile-image-bg-real { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; opacity:0.4; filter: contrast(0.9) grayscale(20%); transition:all .6s ease; z-index:0; }',
    content
)

content = re.sub(
    r'\.brand-tile:hover \.brand-tile-image-bg-real\s*\{\s*opacity:\.18;\s*\}',
    r'.brand-tile:hover .brand-tile-image-bg-real { opacity:0.65; filter: contrast(1.15) grayscale(0%); transform: scale(1.03); }',
    content
)

# Remove the overrides block that forces white text (from .hero-split { background: transparent !important; } down to .brand-tile::after)
# We can do this by regex or careful slicing.
# It seems this block starts around line 1180 and ends around line 1285.
# Let's search for "Nascondiamo l'inner del video originale"
start_match = re.search(r'/\* Nascondiamo l\'inner del video originale \*/', content)
if start_match:
    end_match = re.search(r'\.brand-tile::after\s*\{.*?\}', content[start_match.start():], re.DOTALL)
    if end_match:
        to_remove = content[start_match.start() : start_match.start() + end_match.end()]
        content = content.replace(to_remove, '')

with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v5-VIDEO-FULL.html', 'w', encoding='utf-8') as f:
    f.write(content)

