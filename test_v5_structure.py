from html.parser import HTMLParser

class MyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sections = []

    def handle_starttag(self, tag, attrs):
        if tag == 'section':
            classes = [v for k, v in attrs if k == 'class']
            self.sections.append(classes[0] if classes else '')

p = MyParser()
with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v5-VIDEO-FULL.html', 'r', encoding='utf-8') as f:
    p.feed(f.read())
print("V5 sections:", p.sections)
