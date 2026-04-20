from pathlib import Path

root = Path(r"c:\Users\HP\Desktop\Modzi-Info")

nav = '''<nav class="navbar" aria-label="Navigation principale">
  <div class="navbar__inner">
    <a class="navbar__logo" href="index.html" aria-label="Modzi Info - Accueil">
      <img src="images/logo.png" alt="Modzi Info Logo" width="64" height="64" onerror="this.nextElementSibling.style.display='inline';">
      <span class="navbar__logo-text" style="display:none;">Modzi Info</span>
    </a>
    <ul class="navbar__links" role="list">
      <li><a href="index.html">Accueil</a></li>
      <li><a href="destinations.html">Destinations</a></li>
      <li><a href="articles/index.html">Articles</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul>
    <a href="#" class="btn btn-primary navbar__cta" data-wa-generic style="padding:10px 22px;font-size:0.78rem;"><i class="fas fa-comments"></i> Conseiller</a>
    <button class="hamburger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</nav>
<div class="mobile-menu" role="dialog" aria-modal="true" aria-label="Menu mobile">
  <button class="close-btn" aria-label="Fermer le menu">✕</button>
  <a href="index.html">Accueil</a>
  <a href="destinations.html">Destinations</a>
  <a href="articles/index.html">Articles</a>
  <a href="contact.html">Contact</a>
  <a href="#" class="btn btn-whatsapp" data-wa-generic style="margin-top:16px;"><i class="fas fa-comments"></i> Parler à un conseiller</a>
</div>
'''

footer = '''<footer class="footer">
  <div class="container footer__grid">
    <div class="footer__col">
      <h4>Modzi Info</h4>
      <p>La plateforme de référence pour les étudiants africains souhaitant étudier en Europe et au Canada.</p>
      <div class="footer__social">
        <a href="https://wa.me/22899324636" target="_blank" rel="noopener" aria-label="WhatsApp">
          <i class="fab fa-whatsapp"></i>
        </a>
      </div>
    </div>
    <div class="footer__col">
      <h4>Navigation</h4>
      <ul>
        <li><a href="index.html">Accueil</a></li>
        <li><a href="destinations.html">Destinations</a></li>
        <li><a href="articles/index.html">Articles</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>
    <div class="footer__col">
      <h4>Ressources</h4>
      <ul>
        <li><a href="articles/index.html#modal-visa-etudiant">Guide visa étudiant</a></li>
        <li><a href="articles/index.html#modal-budget-etudes">Budget par pays</a></li>
        <li><a href="articles/index.html#modal-erreurs-visa">Erreurs à éviter</a></li>
        <li><a href="articles/index.html#modal-bourses-africains">Bourses disponibles</a></li>
        <li><a href="articles/index.html#modal-logement-etudiant">Trouver un logement</a></li>
      </ul>
    </div>
    <div class="footer__col">
      <h4>Contact</h4>
      <ul>
        <li><a href="contact.html">Nous contacter</a></li>
        <li><a href="https://wa.me/22899324636" target="_blank" rel="noopener">WhatsApp direct</a></li>
      </ul>
    </div>
  </div>
  <div class="footer__bottom">
    <span>© 2025 Modzi Info. Tous droits réservés.</span>
    <span>Fait avec ❤️ pour les étudiants africains</span>
  </div>
</footer>
'''

country_aside = '''<aside class="sidebar">
        <div class="sidebar-card fade-up">
          <div class="sidebar-card__icon"><i class="fas fa-comments"></i></div>
          <div class="sidebar-card__title">Besoin d'aide pour ton dossier ?</div>
          <p class="sidebar-card__text">Un conseiller te guide dans la sélection du programme, la préparation des documents et la demande de visa.</p>
          <a href="#" class="btn btn-whatsapp" data-wa-country="{country}">Se faire accompagner</a>
        </div>
        <div class="budget-card fade-up">
          <h3><i class="fas fa-wallet"></i> Budget mensuel estimé</h3>
          {budget_lines}
        </div>
      </aside>'''

page_template = '''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="{keywords}">
  <link rel="canonical" href="{canonical}">
  <link rel="stylesheet" href="styles.css">
  <link rel="icon" href="images/logo.png" type="image/png">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  {ld_json}
</head>
<body>
{nav}
<header class="country-hero" aria-labelledby="country-title">
  <div class="country-hero__flag-bg" aria-hidden="true">{flag}</div>
  <div class="container">
    <nav class="breadcrumb" aria-label="Fil d'Ariane">
      <a href="index.html">Accueil</a><span>›</span>
      <a href="destinations.html">Destinations</a><span>›</span>
      <span aria-current="page">{country}</span>
    </nav>
    <div class="country-hero__tag">{tag}</div>
    <h1 class="country-hero__title" id="country-title">{hero_title}</h1>
    <p class="country-hero__subtitle">{hero_subtitle}</p>
    <a href="#" class="btn btn-whatsapp" data-wa-country="{country}">
      <i class="fas fa-comments"></i> Se faire accompagner
    </a>
    <div class="country-hero__quick">
      {quick_stats}
    </div>
  </div>
</header>
<div class="country-content">
  <div class="container">
    <div class="country-layout">
      <main>
        {main_blocks}
      </main>
      {aside}
    </div>
  </div>
</div>
<section class="section section--dark" style="text-align:center;">
  <div class="container">
    <div class="fade-up">
      <div class="tag tag--light">Prêt(e) ?</div>
      <h2 style="font-family:var(--font-display);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--cream);margin-bottom:16px;">Lance ton projet {country} dès aujourd'hui</h2>
      <p style="color:rgba(242,237,230,0.6);margin-bottom:32px;max-width:520px;margin-left:auto;margin-right:auto;">Un conseiller répond à toutes tes questions et t'aide à constituer un dossier solide pour ton projet d'études.</p>
      <a href="#" class="btn btn-whatsapp" data-wa-country="{country}"><i class="fas fa-comments"></i> Se faire accompagner sur WhatsApp</a>
    </div>
  </div>
</section>
{footer}
<script src="main.js"></script>
</body>
</html>
'''

block_template = '''<div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-{icon}"></i></span> {title}</h2>
          {content}
        </div>'''

step_list_template = '''<div class="steps-list">
{items}
          </div>'''

step_item = '''            <div class="step-item">
              <div class="step-item__num">{num}</div>
              <div class="step-item__content">
                <h4>{title}</h4>
                <p>{text}</p>
              </div>
            </div>'''

info_list = '''          <div class="info-list">
{items}
          </div>'''

info_item = '''            <div class="info-item">
              <div class="info-item__icon">{icon}</div>
              <div class="info-item__text">
                <span class="info-item__label">{label}</span>
                {text}
              </div>
            </div>'''

warning_template = '''          <div class="warning-box">
            <div class="warning-box__title">{title}</div>
            <ul>
{items}
            </ul>
          </div>'''

warning_item = '              <li>{text}</li>'

quick_stat = '<div class="quick-stat"><span class="quick-stat__val">{value}</span><span class="quick-stat__key">{label}</span></div>'

pages = []

# France page
fr_quick = ''.join([quick_stat.format(value=v, label=l) for v, l in [('-170€', 'Frais/an (public)'), ('800–1200€', 'Budget mensuel'), ('4–6 mois', 'Délai préparation'), ('12 mois', 'APS après diplôme')]])
fr_main = ''.join([
    block_template.format(icon='bullseye', title='Pourquoi la France ?', content='<p>La France est la destination la plus rassurante pour les étudiants francophones, avec des frais très accessibles et un système bien structuré.</p>'),
    block_template.format(icon='user-graduate', title='Profil idéal', content='<p>La France convient aux étudiants qui veulent une formation universitaire reconnue, un encadrement sécurisé et la possibilité de travailler après les études grâce à l’APS.</p>'),
    block_template.format(icon='clipboard', title='Conditions d’admission', content=info_list.format(items='\n'.join([info_item.format(icon='🎓', label='Niveau requis', text='Baccalauréat ou équivalent pour la licence, licence pour le master.'), info_item.format(icon='📝', label='Campus France', text='Dossier en ligne, entretien et validation du projet d’études.'), info_item.format(icon='🗣️', label='Langue', text='DELF B2 minimum. Formations en anglais acceptent IELTS/TOEFL.'), info_item.format(icon='💰', label='Ressources', text='Justifier 615€/mois ou garant bancaire.')])), ),
    block_template.format(icon='plane', title='Procédure Visa Étudiant', content=step_list_template.format(items='\n'.join([step_item.format(num=i, title=t, text=txt) for i, (t, txt) in enumerate([('Inscription Campus France', 'Créer ton dossier et passer l’entretien avant la date limite.'), ('Candidature', 'Postuler via Parcoursup ou directement selon ton parcours.'), ('Lettre d’admission', 'Obtenir l’admission d’un établissement reconnu.'), ('Demande de VLS-TS', 'Déposer ton dossier au consulat ou via VFS Global.'), ('Validation OFII', 'Valider ton visa à l’arrivée dans les 3 mois.')], start=1)]))),
    block_template.format(icon='exclamation-triangle', title='Erreurs fréquentes', content=warning_template.format(title='À éviter absolument', items='\n'.join([warning_item.format(text=t) for t in ['Poster ton dossier trop tard.', 'Ne pas prouver des ressources suffisantes.', 'Négliger la lettre de motivation.', 'Oublier de valider le VLS-TS.', 'Choisir une formation non reconnue.']]))),
])
fr_budget = '\n'.join([f'          <div class="budget-line"><span class="budget-line__label">{label}</span><span class="budget-line__val">{value}</span></div>' for label, value in [('Logement', '350–600€'), ('Alimentation', '200–300€'), ('Transport', '50–80€'), ('Loisirs', '80–150€'), ('Total estimé', '680–1130€')]])
pages.append((root / 'france.html', page_template.format(title='Étudier en France — Visa, Conditions, Budget | Modzi Info', description='Guide complet pour les étudiants africains souhaitant étudier en France : visa, Campus France, budget et démarches.', keywords='étudier en France, visa étudiant France, Campus France, études Afrique, APS France', canonical='https://modzi.info/france', ld_json='<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Étudier en France : guide complet pour étudiants africains","description":"Visa, Campus France, conditions d\'admission et budget pour étudier en France","author":{"@type":"Organization","name":"Modzi Info"}}</script>', nav=nav, flag='🇫🇷', tag='Destination Europe', hero_title='🇫🇷 Étudier en France', hero_subtitle='Un choix sûr pour les francophones : frais maîtrisés, accompagnement Campus France et un marché européen attractif.', quick_stats=fr_quick, main_blocks=fr_main, aside=country_aside.format(country='France', budget_lines=fr_budget), footer=footer)))

# Allemagne
al_quick = ''.join([quick_stat.format(value=v, label=l) for v, l in [('0€', 'Frais de scolarité'), ('700–1100€', 'Budget mensuel'), ('3–6 mois', 'Délai APS'), ('18 mois', 'Après études')]])
al_main = ''.join([
    block_template.format(icon='bullseye', title='Pourquoi l’Allemagne ?', content='<p>L’Allemagne offre une excellente formation à très faible coût, surtout en ingénierie, sciences et technologies.</p>'),
    block_template.format(icon='user-graduate', title='Profil idéal', content='<p>Pour les étudiants qui veulent une formation reconnue mondialement sans payer de frais élevés.</p>'),
    block_template.format(icon='clipboard', title='Conditions d’admission', content=info_list.format(items='\n'.join([info_item.format(icon='🎓', label='Niveau requis', text='Baccalauréat ou équivalent pour licence, licence pour master.'), info_item.format(icon='📝', label='APS', text='Procédure obligatoire pour les étudiants africains.'), info_item.format(icon='🗣️', label='Langue', text='TestDaF, DSH C1 recommandés; programmes anglais acceptent IELTS/TOEFL.'), info_item.format(icon='💰', label='Ressources', text='Blocage bancaire 11 208€ ou preuve équivalente.')])), ),
    block_template.format(icon='plane', title='Procédure Visa Étudiant', content=step_list_template.format(items='\n'.join([step_item.format(num=i, title=t, text=txt) for i, (t, txt) in enumerate([('Obtenir une admission', 'Candidater auprès d’une université allemande reconnue.'), ('Procédure APS', 'Soumettre ton dossier au consulat et attendre l’approbation.'), ('Blocage bancaire', 'Bloquer 11 208€ ou fournir un garant.');), ('Demande de visa national', 'Déposer le dossier avec tous les justificatifs.');), ('Inscription en Allemagne', 'S’inscrire à l’université et valider le visa localement.')], start=1)]))),
    block_template.format(icon='exclamation-triangle', title='Erreurs fréquentes', content=warning_template.format(title='À éviter absolument', items='\n'.join([warning_item.format(text=t) for t in ['Oublier le blocage bancaire.', 'Choisir une université non accréditée.', 'Sous-estimer le niveau d’allemand.', 'Ne pas préparer l’assurance santé.', 'Postuler trop tard à l’APS.']]))),
])
al_budget = '\n'.join([f'          <div class="budget-line"><span class="budget-line__label">{label}</span><span class="budget-line__val">{value}</span></div>' for label, value in [('Logement', '300–500€'), ('Alimentation', '200–300€'), ('Transport', '50–100€'), ('Loisirs', '80–150€'), ('Total estimé', '630–1050€')]])
pages.append((root / 'allemagne.html', page_template.format(title='Étudier en Allemagne — Visa, Conditions, Budget | Modzi Info', description='Guide pour étudier en Allemagne depuis l’Afrique : admission, APS, visa étudiant et budget.', keywords='étudier en Allemagne, visa étudiant Allemagne, APS, études Afrique, blocage bancaire', canonical='https://modzi.info/allemagne', ld_json='<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Étudier en Allemagne : guide complet pour étudiants africains","description":"Visa, APS, conditions d\'admission et budget pour étudier en Allemagne","author":{"@type":"Organization","name":"Modzi Info"}}</script>', nav=nav, flag='🇩🇪', tag='Destination Europe', hero_title='🇩🇪 Étudier en Allemagne', hero_subtitle='Frais de scolarité gratuits et un permis post-études de 18 mois pour les diplômés internationaux.', quick_stats=al_quick, main_blocks=al_main, aside=country_aside.format(country='Allemagne', budget_lines=al_budget), footer=footer)))
