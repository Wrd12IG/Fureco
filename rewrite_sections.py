import re

with open("wireframe-v5-VIDEO-FULL.html", "r") as f:
    html = f.read()

# 1. Update Heritage (remove stats, rewrite text, keep image layout)
heritage_pattern = r'<section class="below-hero ">\s*<div class="heritage">.*?<div class="heritage-content">.*?</div>\s*</div>\s*</section>'

new_heritage = """<section class="below-hero ">
    <div class="heritage">
      <span class="heritage-decoration">1924</span>
      <div class="heritage-image heritage-image-real">
        <img src="L'arte della pellicceria/img-storia_small.jpg" alt="Storia Fureco" style="object-fit:cover; width:100%; aspect-ratio:4/3; border:1px solid var(--line);">
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
          <img src="L'arte della pellicceria/01_img_furecoworld-1.jpg" alt="Fureco World 1" style="object-fit:cover; width:100%; aspect-ratio:1/1; border:1px solid var(--line);">
          <img src="L'arte della pellicceria/02_img_furecoworld.jpg" alt="Fureco World 2" style="object-fit:cover; width:100%; aspect-ratio:1/1; border:1px solid var(--line);">
        </div>
      </div>
      <div class="heritage-content">
        <div class="heritage-eyebrow">— 03  ·  Heritage</div>
        <h2 class="heritage-title">L'arte della<br/>pellicceria<br/><em>dal 1924.</em></h2>
        <p class="heritage-text">Oltre un secolo di eccellenza sartoriale. La storia di Fureco nasce nei primi anni '20, quando Cesare Gavazzi avviò un esclusivo atelier a Seregno. Oggi, quattro generazioni dopo, l'azienda continua a rappresentare il puro artigianato italiano nel mondo.</p>
        <p class="heritage-text">Sotto la guida dei fratelli Gavazzi — <em>Cesare</em> (CEO), <em>Fabio</em> (Direttore Creativo) e <em>Alberto</em> (Commercial Manager) — ogni capo viene pensato, disegnato e realizzato a mano in Italia, garantendo una qualità e una tracciabilità senza compromessi.</p>
      </div>
    </div>
  </section>"""
html = re.sub(heritage_pattern, new_heritage, html, flags=re.DOTALL)


# 2. Extract Servizi and Showroom
servizi_pattern = r'(<!-- SEZIONE 04 — SERVIZI -->.*?</section>)'
showroom_pattern = r'(<!-- SEZIONE 05 — SHOWROOM -->.*?</section>)'

servizi_match = re.search(servizi_pattern, html, flags=re.DOTALL)
showroom_match = re.search(showroom_pattern, html, flags=re.DOTALL)

servizi_html = servizi_match.group(1)
showroom_html = showroom_match.group(1)

# Remove them from current position
html = html.replace(servizi_html, "")
html = html.replace(showroom_html, "")

# 3. Create Shop and Furmark html
shop_html = """<!-- SEZIONE 05 — SHOP -->
  <section class="below-hero ">
    <div class="section-header">
      <div class="section-number">— 05</div>
      <div class="section-title-group">
        <h2 class="section-title">Online <em>Boutique</em></h2>
        <span class="section-link">Visita lo shop online</span>
      </div>
    </div>
    <div style="position:relative; width:100%; aspect-ratio:24/9; background:#f4f4f4; overflow:hidden; border:1px solid var(--line); display:flex; align-items:center; justify-content:center;">
      <img src="Home/home-2.jpg.webp" alt="Fureco Shop Online" style="position:absolute; width:100%; height:100%; object-fit:cover; opacity:0.9;">
      <div style="position:relative; z-index:2; text-align:center; padding: 48px; background: rgba(250,250,248,0.95); border: 1px solid var(--line);">
        <h3 style="font-size:26px; font-weight:300; margin-bottom:16px;">Le nostre creazioni, direttamente a casa tua.</h3>
        <p style="font-size:14px; color:var(--gray-2); margin-bottom:28px; max-width:440px; margin-left:auto; margin-right:auto;">Esplora l'universo Fureco. Acquista comodamente online le nuove collezioni di pellicceria, cashmere, accessori e articoli per la casa. Spedizione sicura e gratuita in tutto il mondo.</p>
        <button class="btn-primary">Esplora lo Shop</button>
      </div>
    </div>
  </section>"""

furmark_html = """<!-- SEZIONE 07 — FURMARK -->
  <section class="below-hero ">
    <div class="section-header">
      <div class="section-number">— 07</div>
      <div class="section-title-group">
        <h2 class="section-title">Certificazione <em>Furmark®</em></h2>
        <span class="section-link">Sostenibilità</span>
      </div>
    </div>
    <div style="display:flex; gap:48px; align-items:center; border: 1px solid var(--line); padding: 56px; background: var(--white);">
      <div style="flex: 0 0 160px; text-align:center;">
        <h2 style="font-family:'Cormorant Garamond', serif; font-size:42px; font-style:italic; color:var(--tortora-deep); margin:0;">Furmark</h2>
      </div>
      <div style="flex: 1; padding-left: 48px; border-left: 1px solid var(--line-soft);">
        <h3 style="font-size:20px; font-weight:300; margin-bottom:12px;">Sostenibilità e tracciabilità globale</h3>
        <p style="font-size:14px; color:var(--gray-2); line-height:1.6; max-width: 600px;">Tutti i capi Fureco aderiscono al programma globale Furmark®, la certificazione internazionale che garantisce il massimo rispetto degli standard ambientali e del benessere animale. Ogni fase, dall'origine della materia prima fino al capo finito, è tracciabile e certificata in modo indipendente per assicurare trasparenza assoluta.</p>
      </div>
    </div>
  </section>"""

# 4. Re-insert in correct order: Showroom (04) -> Shop (05) -> Servizi (06) -> Furmark (07)
# Note: we need to update the section-number in showroom_html and servizi_html
showroom_html = showroom_html.replace('— 05', '— 04')
servizi_html = servizi_html.replace('— 04', '— 06')

new_blocks = showroom_html + "\n\n  " + shop_html + "\n\n  " + servizi_html + "\n\n  " + furmark_html + "\n\n"

# Insert just before NEWSLETTER
html = html.replace('<!-- NEWSLETTER -->', new_blocks + '  <!-- NEWSLETTER -->')

# 5. Update Footer icons
old_social = """<div class="footer-social">
        <span>IG</span>
        <span>in</span>
      </div>"""
new_social = """<div class="footer-social">
        <a href="#" aria-label="Instagram" style="border: 1px solid var(--line); width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; color: var(--gray-2); transition: all 0.3s;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
        <a href="#" aria-label="LinkedIn" style="border: 1px solid var(--line); width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; color: var(--gray-2); transition: all 0.3s;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
      </div>"""
html = html.replace(old_social, new_social)

# 6. Update Annotations Panel
old_panel = """<div class=" s-panel">
  <h5>STRUTTURA COMPLETA</h5>
  <ul>
    <li><span class="num">01</span>Utility bar</li>
    <li><span class="num">02</span>Nav logo centrato</li>
    <li><span class="num">03</span>HERO 50/50 split</li>
    <li><span class="num">04</span>4 brand tiles (a/b/c/d)</li>
    <li><span class="num">05</span>Collezioni Donna+Uomo</li>
    <li><span class="num">06</span>Heritage 1924</li>
    <li><span class="num">07</span>Servizi unificati ×4</li>
    <li><span class="num">08</span>Showroom Milano+Seregno</li>
    <li><span class="num">09</span>Press marquee</li>
    <li><span class="num">10</span>Newsletter</li>
    <li><span class="num">11</span>Footer 5 colonne</li>
  </ul>
</div>"""
new_panel = """<div class=" s-panel">
  <h5>NUOVA STRUTTURA</h5>
  <ul>
    <li><span class="num">01</span>Utility bar & Nav</li>
    <li><span class="num">02</span>HERO (Video + 4 Brands)</li>
    <li><span class="num">03</span>Collezioni Donna+Uomo</li>
    <li><span class="num">04</span>Heritage 1924</li>
    <li><span class="num">05</span>Showroom</li>
    <li><span class="num">06</span>Online Shop</li>
    <li><span class="num">07</span>Servizi Esclusivi</li>
    <li><span class="num">08</span>Certificazione Furmark</li>
    <li><span class="num">09</span>Newsletter</li>
    <li><span class="num">10</span>Footer Modernizzato</li>
  </ul>
</div>"""
html = html.replace(old_panel, new_panel)

with open("wireframe-v5-VIDEO-FULL.html", "w") as f:
    f.write(html)

print("SCRIPT COMPLETED")
