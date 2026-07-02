with open('/Volumes/Archivio/FURECO/BRAND/materiale sito/wireframe-v6-FINAL.html', 'r', encoding='utf-8') as f:
    v6 = f.read()

# Let's see what CSS is currently inside v6. 
# Did my previous script fail to replace?
import re
print("CSS in v6:")
print(v6.find('HERO 50/50 SPLIT'))
print(v6.find('VIDEO FULL WIDTH'))
