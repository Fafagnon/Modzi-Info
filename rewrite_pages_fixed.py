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

country_aside_template = '''<aside class="sidebar">
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

base_html = '''<!DOCTYPE html>
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

section_block = '''<div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-{icon}"></i></span> {title}</h2>
          {content}
        </div>'''

steps_block = '''<div class="steps-list">
{items}
          </div>'''

step_item = '''            <div class="step-item">
              <div class="step-item__num">{num}</div>
              <div class="step-item__content">
                <h4>{title}</h4>
                <p>{text}</p>
              </div>
            </div>'''

info_block = '''          <div class="info-list">
{items}
          </div>'''

info_item = '''            <div class="info-item">
              <div class="info-item__icon">{icon}</div>
              <div class="info-item__text">
                <span class="info-item__label">{label}</span>
                {text}
              </div>
            </div>'''

warning_block = '''          <div class="warning-box">
            <div class="warning-box__title">{title}</div>
            <ul>
{items}
            </ul>
          </div>'''

warning_item = '              <li>{text}</li>'

quick_stat = '<div class="quick-stat"><span class="quick-stat__val">{value}</span><span class="quick-stat__key">{label}</span></div>'


# Helper functions

def build_info(items):
    return info_block.format(items='\n'.join(items))


def build_steps(items):
    return steps_block.format(items='\n'.join(items))


def build_warning(title, items):
    return warning_block.format(title=title, items='\n'.join(items))


def build_quick_stats(stats):
    return ''.join([quick_stat.format(value=value, label=label) for value, label in stats])


def build_country_page(path, title, description, keywords, canonical, flag, tag, hero_title, hero_subtitle, quick_stats, blocks, budget_lines, country):
    aside = country_aside_template.format(country=country, budget_lines='\n'.join([f'          <div class="budget-line"><span class="budget-line__label">{label}</span><span class="budget-line__val">{value}</span></div>' for label, value in budget_lines]))
    content = base_html.format(
        title=title,
        description=description,
        keywords=keywords,
        canonical=canonical,
        ld_json=f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{description}","author":{{"@type":"Organization","name":"Modzi Info"}}}}</script>',
        nav=nav,
        flag=flag,
        tag=tag,
        hero_title=hero_title,
        hero_subtitle=hero_subtitle,
        quick_stats=build_quick_stats(quick_stats),
        main_blocks='\n'.join(blocks),
        aside=aside,
        footer=footer,
        country=country,
    )
    path.write_text(content, encoding='utf-8')


# Destinations page

destinations_html = '''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Destinations pour étudier — Europe et Canada | Modzi Info</title>
  <meta name="description" content="Compare les 5 destinations pour étudier depuis l'Afrique : France, Allemagne, Belgique, Italie, Canada. Choisis selon ton budget, ta langue et ton projet après études.">
  <link rel="canonical" href="https://modzi.info/destinations">
  <link rel="stylesheet" href="styles.css">
  <link rel="icon" href="images/logo.png" type="image/png">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
''' + nav + '''
<header class="page-header" aria-labelledby="dest-title">
  <div class="page-header__bg" aria-hidden="true"></div>
  <div class="container page-header__content">
    <div class="tag tag--light">Destinations</div>
    <h1 class="page-header__title" id="dest-title">Trouve le pays qui va propulser ton projet d’études</h1>
    <p class="page-header__sub">5 destinations phares expliquées pour que tu saches rapidement si c’est mieux d’aller en France, Allemagne, Belgique, Italie ou Canada.</p>
    <a href="#profil" class="btn btn-primary">Je veux choisir mon profil</a>
  </div>
</header>

<section class="section" id="profil">
  <div class="container">
    <div class="fade-up">
      <div class="tag">Quel pays pour toi ?</div>
      <h2 class="section-title">Ton profil oriente ton choix</h2>
      <p class="section-subtitle">Sélectionne ce qui te correspond le mieux pour obtenir une recommandation claire et rapide.</p>
    </div>
    <div class="profile-grid">
      <article class="profile-card fade-up">
        <div class="profile-card__tag">Budget serré</div>
        <h3 class="profile-card__title">Minimise les frais de scolarité</h3>
        <p class="profile-card__text">France, Allemagne et Italie te permettent de limiter le coût de ton projet, avec des frais quasi nuls ou très faibles.</p>
        <div class="profile-card__footer">
          <span class="meta-tag">France</span>
          <span class="meta-tag">Allemagne</span>
          <span class="meta-tag">Italie</span>
        </div>
      </article>
      <article class="profile-card fade-up">
        <div class="profile-card__tag">Francophone</div>
        <h3 class="profile-card__title">Étudier sans changer de langue</h3>
        <p class="profile-card__text">France et Belgique sont les meilleures options si tu veux rester en français tout en accédant à un campus européen.</p>
        <div class="profile-card__footer">
          <span class="meta-tag">France</span>
          <span class="meta-tag">Belgique</span>
        </div>
      </article>
      <article class="profile-card fade-up">
        <div class="profile-card__tag">Long terme</div>
        <h3 class="profile-card__title">Construire une carrière après les études</h3>
        <p class="profile-card__text">Si tu souhaites travailler ensuite, vise le Canada ou l'Allemagne : leurs permis post-diplôme sont très favorables.</p>
        <div class="profile-card__footer">
          <span class="meta-tag">Canada</span>
          <span class="meta-tag">Allemagne</span>
        </div>
      </article>
      <article class="profile-card fade-up">
        <div class="profile-card__tag">Spécialités</div>
        <h3 class="profile-card__title">Tech, ingénierie ou art</h3>
        <p class="profile-card__text">Pour l'ingénierie et la tech, l'Allemagne est une référence. Pour l'art et le design, l'Italie est imbattable.</p>
        <div class="profile-card__footer">
          <span class="meta-tag">Allemagne</span>
          <span class="meta-tag">Italie</span>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section section--beige" id="dest-list">
  <div class="container">
    <div class="fade-up">
      <div class="tag">Comparaison</div>
      <h2 class="section-title">5 pays, 5 forces</h2>
      <p class="section-subtitle">Chaque destination a son ADN : on te montre vite ce qui change vraiment.</p>
    </div>
    <div class="destinations-grid">
      <article class="dest-card fade-up" onclick="window.location='france.html'" tabindex="0" role="button" aria-label="Étudier en France">
        <div class="dest-card__header">
          <img src="images/fr.png" alt="Drapeau France" class="dest-card__flag">
          <div class="dest-card__header-bg" style="background:linear-gradient(135deg,#002395,#fff,#ed2939);"></div>
        </div>
        <div class="dest-card__body">
          <h3 class="dest-card__country">France</h3>
          <p class="dest-card__desc">Le choix le plus rassurant pour les francophones : frais bas, forte culture étudiante, accompagnement Campus France.</p>
          <div class="dest-card__meta">
            <span class="meta-tag">Francophone</span>
            <span class="meta-tag">Campus France</span>
            <span class="meta-tag">APS 12 mois</span>
          </div>
          <a href="france.html" class="btn btn-outline" style="width:100%;justify-content:center;">Voir les conditions →</a>
        </div>
      </article>
      <article class="dest-card fade-up" onclick="window.location='allemagne.html'" tabindex="0" role="button" aria-label="Étudier en Allemagne">
        <div class="dest-card__header">
          <img src="images/de.png" alt="Drapeau Allemagne" class="dest-card__flag">
          <div class="dest-card__header-bg" style="background:linear-gradient(135deg,#000,#dd0000,#ffce00);"></div>
        </div>
        <div class="dest-card__body">
          <h3 class="dest-card__country">Allemagne</h3>
          <p class="dest-card__desc">Formation de très haut niveau, frais presque nuls et un permis de travail post-études de 18 mois.</p>
          <div class="dest-card__meta">
            <span class="meta-tag">Gratuit</span>
            <span class="meta-tag">Tech & ingénierie</span>
            <span class="meta-tag">APS 18 mois</span>
          </div>
          <a href="allemagne.html" class="btn btn-outline" style="width:100%;justify-content:center;">Voir les conditions →</a>
        </div>
      </article>
      <article class="dest-card fade-up" onclick="window.location='belgique.html'" tabindex="0" role="button" aria-label="Étudier en Belgique">
        <div class="dest-card__header">
          <img src="images/be.png" alt="Drapeau Belgique" class="dest-card__flag">
          <div class="dest-card__header-bg" style="background:linear-gradient(135deg,#000,#f00,#fdda24);"></div>
        </div>
        <div class="dest-card__body">
          <h3 class="dest-card__country">Belgique</h3>
          <p class="dest-card__desc">Option francophone en Europe avec des universités réputées et un accès simple à l’espace Schengen.</p>
          <div class="dest-card__meta">
            <span class="meta-tag">Francophone</span>
            <span class="meta-tag">ULB/UCLouvain</span>
            <span class="meta-tag">Visa D</span>
          </div>
          <a href="belgique.html" class="btn btn-outline" style="width:100%;justify-content:center;">Voir les conditions →</a>
        </div>
      </article>
      <article class="dest-card fade-up" onclick="window.location='italie.html'" tabindex="0" role="button" aria-label="Étudier en Italie">
        <div class="dest-card__header">
          <img src="images/it.png" alt="Drapeau Italie" class="dest-card__flag">
          <div class="dest-card__header-bg" style="background:linear-gradient(135deg,#009246,#fff,#ce2b37);"></div>
        </div>
        <div class="dest-card__body">
          <h3 class="dest-card__country">Italie</h3>
          <p class="dest-card__desc">La meilleure destination pour les arts, le design et l’architecture, avec des frais très bas.</p>
          <div class="dest-card__meta">
            <span class="meta-tag">Art & design</span>
            <span class="meta-tag">Frais abordables</span>
            <span class="meta-tag">Visa D</span>
          </div>
          <a href="italie.html" class="btn btn-outline" style="width:100%;justify-content:center;">Voir les conditions →</a>
        </div>
      </article>
      <article class="dest-card fade-up" onclick="window.location='canada.html'" tabindex="0" role="button" aria-label="Étudier au Canada">
        <div class="dest-card__header">
          <img src="images/ca.png" alt="Drapeau Canada" class="dest-card__flag">
          <div class="dest-card__header-bg" style="background:linear-gradient(135deg,#ff0000,#fff,#ff0000);"></div>
        </div>
        <div class="dest-card__body">
          <h3 class="dest-card__country">Canada</h3>
          <p class="dest-card__desc">Le meilleur choix si tu veux poursuivre une carrière et une immigration à plus long terme.</p>
          <div class="dest-card__meta">
            <span class="meta-tag">Immigration</span>
            <span class="meta-tag">PGWP 3 ans</span>
            <span class="meta-tag">Bilingue</span>
          </div>
          <a href="canada.html" class="btn btn-outline" style="width:100%;justify-content:center;">Voir les conditions →</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section" id="comparison">
  <div class="container">
    <div class="fade-up">
      <div class="tag">Comparatif rapide</div>
      <h2 class="section-title">Le match final</h2>
      <p class="section-subtitle">Un tableau simple pour faire la différence entre les destinations les plus recherchées.</p>
    </div>
    <div class="fade-up" style="overflow-x:auto; margin-top:32px;">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Pays</th>
            <th>Frais</th>
            <th>Langue</th>
            <th>Budget</th>
            <th>Après études</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>France</td>
            <td>~170€/an</td>
            <td>Français</td>
            <td>800–1200€</td>
            <td>APS 12 mois</td>
          </tr>
          <tr>
            <td>Allemagne</td>
            <td>0€ - 350€/sem</td>
            <td>Allemand / Anglais</td>
            <td>700–1100€</td>
            <td>18 mois</td>
          </tr>
          <tr>
            <td>Belgique</td>
            <td>835–4000€/an</td>
            <td>Français / Néerlandais</td>
            <td>900–1300€</td>
            <td>Visa D</td>
          </tr>
          <tr>
            <td>Italie</td>
            <td>900–3000€/an</td>
            <td>Italien / Anglais</td>
            <td>700–1000€</td>
            <td>Visa D</td>
          </tr>
          <tr>
            <td>Canada</td>
            <td>8 000–20 000$/an</td>
            <td>Français / Anglais</td>
            <td>1200–2000$</td>
            <td>PGWP 3 ans</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section--dark" style="text-align:center;">
  <div class="container">
    <div class="fade-up">
      <div class="tag tag--light">Choix</div>
      <h2 style="font-family:var(--font-display);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--cream);margin-bottom:16px;">Tu sais déjà où tu veux aller ?</h2>
      <p style="color:rgba(242,237,230,0.6);margin-bottom:32px;max-width:560px;margin-left:auto;margin-right:auto;">Si tu hésites encore, parle avec un conseiller pour faire le point sur ton profil, ton budget et tes priorités.</p>
      <a href="#" class="btn btn-whatsapp" data-wa-generic><i class="fas fa-comments"></i> Parler à un conseiller WhatsApp</a>
    </div>
  </div>
</section>

''' + footer + '''
<script src="main.js"></script>
</body>
</html>'''

Path(root / 'destinations.html').write_text(destinations_html, encoding='utf-8')

# Country pages definitions

france_html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Étudier en France — Visa, Conditions, Budget | Modzi Info</title>
  <meta name="description" content="Guide complet pour les étudiants africains souhaitant étudier en France : visa, Campus France, budget et démarches.">
  <meta name="keywords" content="étudier en France, visa étudiant France, Campus France, études Afrique, APS France">
  <link rel="canonical" href="https://modzi.info/france">
  <link rel="stylesheet" href="styles.css">
  <link rel="icon" href="images/logo.png" type="image/png">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"Étudier en France : guide complet pour étudiants africains","description":"Visa, Campus France, conditions d'admission et budget pour étudier en France","author":{{"@type":"Organization","name":"Modzi Info"}}}}</script>
</head>
<body>
{nav}
<header class="country-hero" aria-labelledby="country-title">
  <div class="country-hero__flag-bg" aria-hidden="true">🇫🇷</div>
  <div class="container">
    <nav class="breadcrumb" aria-label="Fil d'Ariane">
      <a href="index.html">Accueil</a><span>›</span>
      <a href="destinations.html">Destinations</a><span>›</span>
      <span aria-current="page">France</span>
    </nav>
    <div class="country-hero__tag">Destination Europe</div>
    <h1 class="country-hero__title" id="country-title">🇫🇷 Étudier en France</h1>
    <p class="country-hero__subtitle">Un choix sûr pour les francophones : frais maîtrisés, accompagnement Campus France et un marché européen attractif.</p>
    <a href="#" class="btn btn-whatsapp" data-wa-country="France">
      <i class="fas fa-comments"></i> Se faire accompagner
    </a>
    <div class="country-hero__quick">
      <div class="quick-stat"><span class="quick-stat__val">~170€</span><span class="quick-stat__key">Frais/an (public)</span></div>
      <div class="quick-stat"><span class="quick-stat__val">800–1200€</span><span class="quick-stat__key">Budget mensuel</span></div>
      <div class="quick-stat"><span class="quick-stat__val">4–6 mois</span><span class="quick-stat__key">Délai préparation</span></div>
      <div class="quick-stat"><span class="quick-stat__val">12 mois</span><span class="quick-stat__key">APS après diplôme</span></div>
    </div>
  </div>
</header>
<div class="country-content">
  <div class="container">
    <div class="country-layout">
      <main>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-bullseye"></i></span> Pourquoi la France ?</h2>
          <p>La France est la destination la plus rassurante pour les étudiants francophones, avec des frais très accessibles et un système bien structuré.</p>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-user-graduate"></i></span> Profil idéal</h2>
          <p>La France convient aux étudiants qui veulent une formation universitaire reconnue, un encadrement sécurisé et la possibilité de travailler après les études grâce à l’APS.</p>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-clipboard"></i></span> Conditions d’admission</h2>
          <div class="info-list">
            <div class="info-item">
              <div class="info-item__icon">🎓</div>
              <div class="info-item__text">
                <span class="info-item__label">Niveau requis</span>
                Baccalauréat ou équivalent pour la licence, licence pour le master.
              </div>
            </div>
            <div class="info-item">
              <div class="info-item__icon">📝</div>
              <div class="info-item__text">
                <span class="info-item__label">Campus France</span>
                Dossier en ligne, entretien et validation du projet d’études.
              </div>
            </div>
            <div class="info-item">
              <div class="info-item__icon">🗣️</div>
              <div class="info-item__text">
                <span class="info-item__label">Langue</span>
                DELF B2 minimum. Formations en anglais acceptent IELTS/TOEFL.
              </div>
            </div>
            <div class="info-item">
              <div class="info-item__icon">💰</div>
              <div class="info-item__text">
                <span class="info-item__label">Ressources</span>
                Justifier 615€/mois ou garant bancaire.
              </div>
            </div>
          </div>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-plane"></i></span> Procédure Visa Étudiant</h2>
          <div class="steps-list">
            <div class="step-item">
              <div class="step-item__num">1</div>
              <div class="step-item__content">
                <h4>Inscription Campus France</h4>
                <p>Créer ton dossier et passer l’entretien avant la date limite.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">2</div>
              <div class="step-item__content">
                <h4>Candidature</h4>
                <p>Postuler via Parcoursup ou directement selon ton parcours.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">3</div>
              <div class="step-item__content">
                <h4>Lettre d’admission</h4>
                <p>Obtenir l’admission d’un établissement reconnu.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">4</div>
              <div class="step-item__content">
                <h4>Demande de VLS-TS</h4>
                <p>Déposer ton dossier au consulat ou via VFS Global.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">5</div>
              <div class="step-item__content">
                <h4>Validation OFII</h4>
                <p>Valider ton visa à l’arrivée dans les 3 mois.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-exclamation-triangle"></i></span> Erreurs fréquentes</h2>
          <div class="warning-box">
            <div class="warning-box__title">À éviter absolument</div>
            <ul>
              <li>Poster ton dossier trop tard.</li>
              <li>Ne pas prouver des ressources suffisantes.</li>
              <li>Négliger la lettre de motivation.</li>
              <li>Oublier de valider le VLS-TS.</li>
              <li>Choisir une formation non reconnue.</li>
            </ul>
          </div>
        </div>
      </main>
      ''' + country_aside_template.format(country='France', budget_lines='          <div class="budget-line"><span class="budget-line__label">Logement</span><span class="budget-line__val">350–600€</span></div>\n          <div class="budget-line"><span class="budget-line__label">Alimentation</span><span class="budget-line__val">200–300€</span></div>\n          <div class="budget-line"><span class="budget-line__label">Transport</span><span class="budget-line__val">50–80€</span></div>\n          <div class="budget-line"><span class="budget-line__label">Loisirs</span><span class="budget-line__val">80–150€</span></div>\n          <div class="budget-line"><span class="budget-line__label">Total estimé</span><span class="budget-line__val">680–1130€</span></div>') + '''
    </div>
  </div>
</div>
<section class="section section--dark" style="text-align:center;">
  <div class="container">
    <div class="fade-up">
      <div class="tag tag--light">Prêt(e) ?</div>
      <h2 style="font-family:var(--font-display);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--cream);margin-bottom:16px;">Lance ton projet France dès aujourd'hui</h2>
      <p style="color:rgba(242,237,230,0.6);margin-bottom:32px;max-width:520px;margin-left:auto;margin-right:auto;">Un conseiller répond à toutes tes questions et t'aide à constituer un dossier solide pour ton projet d'études.</p>
      <a href="#" class="btn btn-whatsapp" data-wa-country="France"><i class="fas fa-comments"></i> Se faire accompagner sur WhatsApp</a>
    </div>
  </div>
</section>
''' + footer + '''
<script src="main.js"></script>
</body>
</html>'''

Path(root / 'france.html').write_text(france_html, encoding='utf-8')

# Germany page
allemagne_html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Étudier en Allemagne — Visa, Conditions, Budget | Modzi Info</title>
  <meta name="description" content="Guide pour étudier en Allemagne depuis l’Afrique : admission, APS, visa étudiant et budget.">
  <meta name="keywords" content="étudier en Allemagne, visa étudiant Allemagne, APS, études Afrique, blocage bancaire">
  <link rel="canonical" href="https://modzi.info/allemagne">
  <link rel="stylesheet" href="styles.css">
  <link rel="icon" href="images/logo.png" type="image/png">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"Étudier en Allemagne : guide complet pour étudiants africains","description":"Visa, APS, conditions d'admission et budget pour étudier en Allemagne","author":{{"@type":"Organization","name":"Modzi Info"}}}}</script>
</head>
<body>
{nav}
<header class="country-hero" aria-labelledby="country-title">
  <div class="country-hero__flag-bg" aria-hidden="true">🇩🇪</div>
  <div class="container">
    <nav class="breadcrumb" aria-label="Fil d'Ariane">
      <a href="index.html">Accueil</a><span>›</span>
      <a href="destinations.html">Destinations</a><span>›</span>
      <span aria-current="page">Allemagne</span>
    </nav>
    <div class="country-hero__tag">Destination Europe</div>
    <h1 class="country-hero__title" id="country-title">🇩🇪 Étudier en Allemagne</h1>
    <p class="country-hero__subtitle">Frais de scolarité gratuits et un permis post-études de 18 mois, idéal pour les filières technologiques.</p>
    <a href="#" class="btn btn-whatsapp" data-wa-country="Allemagne">
      <i class="fas fa-comments"></i> Se faire accompagner
    </a>
    <div class="country-hero__quick">
      <div class="quick-stat"><span class="quick-stat__val">0€</span><span class="quick-stat__key">Frais de scolarité</span></div>
      <div class="quick-stat"><span class="quick-stat__val">700–1100€</span><span class="quick-stat__key">Budget mensuel</span></div>
      <div class="quick-stat"><span class="quick-stat__val">3–6 mois</span><span class="quick-stat__key">Délai APS</span></div>
      <div class="quick-stat"><span class="quick-stat__val">18 mois</span><span class="quick-stat__key">Après études</span></div>
    </div>
  </div>
</header>
<div class="country-content">
  <div class="container">
    <div class="country-layout">
      <main>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-bullseye"></i></span> Pourquoi l’Allemagne ?</h2>
          <p>L’Allemagne offre une excellente formation à très faible coût, surtout en ingénierie, sciences et technologies.</p>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-user-graduate"></i></span> Profil idéal</h2>
          <p>Pour les étudiants qui veulent une formation reconnue mondialement sans payer de frais élevés.</p>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-clipboard"></i></span> Conditions d’admission</h2>
          <div class="info-list">
            <div class="info-item">
              <div class="info-item__icon">🎓</div>
              <div class="info-item__text">
                <span class="info-item__label">Niveau requis</span>
                Baccalauréat ou équivalent pour licence, licence pour master.
              </div>
            </div>
            <div class="info-item">
              <div class="info-item__icon">📝</div>
              <div class="info-item__text">
                <span class="info-item__label">APS</span>
                Procédure obligatoire pour les étudiants africains.
              </div>
            </div>
            <div class="info-item">
              <div class="info-item__icon">🗣️</div>
              <div class="info-item__text">
                <span class="info-item__label">Langue</span>
                TestDaF, DSH C1 recommandés; programmes anglais acceptent IELTS/TOEFL.
              </div>
            </div>
            <div class="info-item">
              <div class="info-item__icon">💰</div>
              <div class="info-item__text">
                <span class="info-item__label">Ressources</span>
                Blocage bancaire 11 208€ ou preuve équivalente.
              </div>
            </div>
          </div>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-plane"></i></span> Procédure Visa Étudiant</h2>
          <div class="steps-list">
            <div class="step-item">
              <div class="step-item__num">1</div>
              <div class="step-item__content">
                <h4>Obtenir une admission</h4>
                <p>Candidater auprès d’une université allemande reconnue.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">2</div>
              <div class="step-item__content">
                <h4>Procédure APS</h4>
                <p>Soumettre ton dossier au consulat et attendre l’approbation.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">3</div>
              <div class="step-item__content">
                <h4>Blocage bancaire</h4>
                <p>Bloquer 11 208€ ou fournir un garant.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">4</div>
              <div class="step-item__content">
                <h4>Demande de visa</h4>
                <p>Déposer le dossier avec tous les justificatifs.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">5</div>
              <div class="step-item__content">
                <h4>Inscription en Allemagne</h4>
                <p>S’inscrire à l’université et valider le visa localement.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-exclamation-triangle"></i></span> Erreurs fréquentes</h2>
          <div class="warning-box">
            <div class="warning-box__title">À éviter absolument</div>
            <ul>
              <li>Oublier le blocage bancaire.</li>
              <li>Choisir une université non accréditée.</li>
              <li>Sous-estimer le niveau d’allemand.</li>
              <li>Ne pas préparer l’assurance santé.</li>
              <li>Postuler trop tard à l’APS.</li>
            </ul>
          </div>
        </div>
      </main>
      ''' + country_aside_template.format(country='Allemagne', budget_lines='          <div class="budget-line"><span class="budget-line__label">Logement</span><span class="budget-line__val">300–500€</span></div>\n          <div class="budget-line"><span class="budget-line__label">Alimentation</span><span class="budget-line__val">200–300€</span></div>\n          <div class="budget-line"><span class="budget-line__label">Transport</span><span class="budget-line__val">50–100€</span></div>\n          <div class="budget-line"><span class="budget-line__label">Loisirs</span><span class="budget-line__val">80–150€</span></div>\n          <div class="budget-line"><span class="budget-line__label">Total estimé</span><span class="budget-line__val">630–1050€</span></div>') + '''
    </div>
  </div>
</div>
<section class="section section--dark" style="text-align:center;">
  <div class="container">
    <div class="fade-up">
      <div class="tag tag--light">Prêt(e) ?</div>
      <h2 style="font-family:var(--font-display);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--cream);margin-bottom:16px;">Lance ton projet Allemagne dès aujourd'hui</h2>
      <p style="color:rgba(242,237,230,0.6);margin-bottom:32px;max-width:520px;margin-left:auto;margin-right:auto;">Un conseiller répond à toutes tes questions et t'aide à constituer un dossier solide pour ton projet d'études en Allemagne.</p>
      <a href="#" class="btn btn-whatsapp" data-wa-country="Allemagne"><i class="fas fa-comments"></i> Se faire accompagner sur WhatsApp</a>
    </div>
  </div>
</section>
''' + footer + '''
<script src="main.js"></script>
</body>
</html>'''

Path(root / 'allemagne.html').write_text(allemagne_html, encoding='utf-8')

# Belgique page
belgique_html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Étudier en Belgique — Visa, Conditions, Budget | Modzi Info</title>
  <meta name="description" content="Guide pour étudier en Belgique depuis l’Afrique : admission, visa étudiant et budget.">
  <meta name="keywords" content="étudier en Belgique, visa étudiant Belgique, université Belgique, études Afrique, CESS Belgique">
  <link rel="canonical" href="https://modzi.info/belgique">
  <link rel="stylesheet" href="styles.css">
  <link rel="icon" href="images/logo.png" type="image/png">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"Étudier en Belgique : guide complet pour étudiants africains","description":"Visa, conditions d'admission et budget pour étudier en Belgique","author":{{"@type":"Organization","name":"Modzi Info"}}}}</script>
</head>
<body>
{nav}
<header class="country-hero" aria-labelledby="country-title">
  <div class="country-hero__flag-bg" aria-hidden="true">🇧🇪</div>
  <div class="container">
    <nav class="breadcrumb" aria-label="Fil d'Ariane">
      <a href="index.html">Accueil</a><span>›</span>
      <a href="destinations.html">Destinations</a><span>›</span>
      <span aria-current="page">Belgique</span>
    </nav>
    <div class="country-hero__tag">Destination Europe</div>
    <h1 class="country-hero__title" id="country-title">🇧🇪 Étudier en Belgique</h1>
    <p class="country-hero__subtitle">Une destination francophone avec un excellent rapport qualité/prix et un accès simple à l’espace Schengen.</p>
    <a href="#" class="btn btn-whatsapp" data-wa-country="Belgique">
      <i class="fas fa-comments"></i> Se faire accompagner
    </a>
    <div class="country-hero__quick">
      <div class="quick-stat"><span class="quick-stat__val">835–4000€</span><span class="quick-stat__key">Frais annuels</span></div>
      <div class="quick-stat"><span class="quick-stat__val">900–1300€</span><span class="quick-stat__key">Budget mensuel</span></div>
      <div class="quick-stat"><span class="quick-stat__val">3–4 mois</span><span class="quick-stat__key">Délai préparation</span></div>
      <div class="quick-stat"><span class="quick-stat__val">Visa D</span><span class="quick-stat__key">Type de visa</span></div>
    </div>
  </div>
</header>
<div class="country-content">
  <div class="container">
    <div class="country-layout">
      <main>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-bullseye"></i></span> Pourquoi la Belgique ?</h2>
          <p>La Belgique combine un environnement francophone, des universités solides et une expérience européenne accessible.</p>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-user-graduate"></i></span> Profil idéal</h2>
          <p>Idéale pour les francophones qui veulent une formation reconnue en Europe sans changer de langue ni de cadre culturel.</p>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-clipboard"></i></span> Conditions d’admission</h2>
          <div class="info-list">
            <div class="info-item">
              <div class="info-item__icon">🎓</div>
              <div class="info-item__text">
                <span class="info-item__label">Niveau requis</span>
                CESS ou équivalent pour l’accès aux études supérieures.
              </div>
            </div>
            <div class="info-item">
              <div class="info-item__icon">📝</div>
              <div class="info-item__text">
                <span class="info-item__label">Procédure</span>
                Candidature directe auprès des universités, parfois concours ou examens.
              </div>
            </div>
            <div class="info-item">
              <div class="info-item__icon">🗣️</div>
              <div class="info-item__text">
                <span class="info-item__label">Langue</span>
                Français courant pour les programmes francophones. Certains cours en anglais ou néerlandais.
              </div>
            </div>
            <div class="info-item">
              <div class="info-item__icon">💰</div>
              <div class="info-item__text">
                <span class="info-item__label">Ressources</span>
                Blocage de compte 6 180€ ou garant bancaire.
              </div>
            </div>
          </div>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-plane"></i></span> Procédure Visa Étudiant</h2>
          <div class="steps-list">
            <div class="step-item">
              <div class="step-item__num">1</div>
              <div class="step-item__content">
                <h4>Obtenir une lettre d’admission</h4>
                <p>Candidater auprès d’une université belge reconnue.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">2</div>
              <div class="step-item__content">
                <h4>Préparer les justificatifs financiers</h4>
                <p>Bloquer 6 180€ ou garantir le financement avec un garant.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">3</div>
              <div class="step-item__content">
                <h4>Réunir les documents</h4>
                <p>Passeport, assurance santé, justificatifs scolaires, preuve de fonds.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">4</div>
              <div class="step-item__content">
                <h4>Demande de visa type D</h4>
                <p>Déposer au consulat ou via un centre VFS.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">5</div>
              <div class="step-item__content">
                <h4>Inscription</h4>
                <p>S’inscrire à l’université et valider ton visa à l’arrivée.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-exclamation-triangle"></i></span> Erreurs fréquentes</h2>
          <div class="warning-box">
            <div class="warning-box__title">À éviter absolument</div>
            <ul>
              <li>Choisir une université non reconnue.</li>
              <li>Présenter des ressources financières insuffisantes.</li>
              <li>Négliger l’assurance santé obligatoire.</li>
              <li>Oublier de valider le visa à l’arrivée.</li>
              <li>Confondre les régions linguistiques.</li>
            </ul>
          </div>
        </div>
      </main>
      ''' + country_aside_template.format(country='Belgique', budget_lines='          <div class="budget-line"><span class="budget-line__label">Logement</span><span class="budget-line__val">400–600€</span></div>\n          <div class="budget-line"><span class="budget-line__label">Alimentation</span><span class="budget-line__val">250–350€</span></div>\n          <div class="budget-line"><span class="budget-line__label">Transport</span><span class="budget-line__val">50–80€</span></div>\n          <div class="budget-line"><span class="budget-line__label">Loisirs</span><span class="budget-line__val">100–150€</span></div>\n          <div class="budget-line"><span class="budget-line__label">Total estimé</span><span class="budget-line__val">800–1180€</span></div>') + '''
    </div>
  </div>
</div>
<section class="section section--dark" style="text-align:center;">
  <div class="container">
    <div class="fade-up">
      <div class="tag tag--light">Prêt(e) ?</div>
      <h2 style="font-family:var(--font-display);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--cream);margin-bottom:16px;">Lance ton projet Belgique dès aujourd'hui</h2>
      <p style="color:rgba(242,237,230,0.6);margin-bottom:32px;max-width:520px;margin-left:auto;margin-right:auto;">Un conseiller répond à toutes tes questions et t'aide à constituer un dossier solide pour ton projet d'études en Belgique.</p>
      <a href="#" class="btn btn-whatsapp" data-wa-country="Belgique"><i class="fas fa-comments"></i> Se faire accompagner sur WhatsApp</a>
    </div>
  </div>
</section>
''' + footer + '''
<script src="main.js"></script>
</body>
</html>'''

Path(root / 'belgique.html').write_text(belgique_html, encoding='utf-8')

# Italie page
italie_html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Étudier en Italie — Visa, Conditions, Budget | Modzi Info</title>
  <meta name="description" content="Guide pour étudier en Italie depuis l’Afrique : admission, visa étudiant et budget.">
  <meta name="keywords" content="étudier en Italie, visa étudiant Italie, études Afrique, portfolio artistique, Visa D">
  <link rel="canonical" href="https://modzi.info/italie">
  <link rel="stylesheet" href="styles.css">
  <link rel="icon" href="images/logo.png" type="image/png">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"Étudier en Italie : guide complet pour étudiants africains","description":"Visa, conditions d'admission et budget pour étudier en Italie","author":{{"@type":"Organization","name":"Modzi Info"}}}}</script>
</head>
<body>
{nav}
<header class="country-hero" aria-labelledby="country-title">
  <div class="country-hero__flag-bg" aria-hidden="true">🇮🇹</div>
  <div class="container">
    <nav class="breadcrumb" aria-label="Fil d'Ariane">
      <a href="index.html">Accueil</a><span>›</span>
      <a href="destinations.html">Destinations</a><span>›</span>
      <span aria-current="page">Italie</span>
    </nav>
    <div class="country-hero__tag">Destination Europe</div>
    <h1 class="country-hero__title" id="country-title">🇮🇹 Étudier en Italie</h1>
    <p class="country-hero__subtitle">Destination idéale pour l’art, le design, l’architecture et l’ingénierie à frais maîtrisés.</p>
    <a href="#" class="btn btn-whatsapp" data-wa-country="Italie">
      <i class="fas fa-comments"></i> Se faire accompagner
    </a>
    <div class="country-hero__quick">
      <div class="quick-stat"><span class="quick-stat__val">900–3000€</span><span class="quick-stat__key">Frais annuels</span></div>
      <div class="quick-stat"><span class="quick-stat__val">700–1000€</span><span class="quick-stat__key">Budget mensuel</span></div>
      <div class="quick-stat"><span class="quick-stat__val">Visa D</span><span class="quick-stat__key">Type de visa</span></div>
      <div class="quick-stat"><span class="quick-stat__val">Art & Design</span><span class="quick-stat__key">Spécialités</span></div>
    </div>
  </div>
</header>
<div class="country-content">
  <div class="container">
    <div class="country-layout">
      <main>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-bullseye"></i></span> Pourquoi l’Italie ?</h2>
          <p>L’Italie est parfaite pour les filières créatives et techniques : art, design, architecture, mode et ingénierie.</p>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-user-graduate"></i></span> Profil idéal</h2>
          <p>Pour les étudiants qui veulent une formation artistique dans un cadre culturel riche, avec des frais de scolarité compétitifs.</p>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-clipboard"></i></span> Conditions d’admission</h2>
          <div class="info-list">
            <div class="info-item">
              <div class="info-item__icon">🎓</div>
              <div class="info-item__text">
                <span class="info-item__label">Niveau requis</span>
                Baccalauréat ou équivalent pour licence, Bac+3 pour master.
              </div>
            </div>
            <div class="info-item">
              <div class="info-item__icon">📝</div>
              <div class="info-item__text">
                <span class="info-item__label">Langue</span>
                CILS/CELI pour l’italien, IELTS/TOEFL pour l’anglais.
              </div>
            </div>
            <div class="info-item">
              <div class="info-item__icon">🖼️</div>
              <div class="info-item__text">
                <span class="info-item__label">Portfolio</span>
                Souvent nécessaire pour les programmes d’art, design et architecture.
              </div>
            </div>
            <div class="info-item">
              <div class="info-item__icon">💰</div>
              <div class="info-item__text">
                <span class="info-item__label">Ressources</span>
                Blocage bancaire de 6 000€ par an ou garant bancaire.
              </div>
            </div>
          </div>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-plane"></i></span> Procédure Visa Étudiant</h2>
          <div class="steps-list">
            <div class="step-item">
              <div class="step-item__num">1</div>
              <div class="step-item__content">
                <h4>Obtenir une admission</h4>
                <p>Candidater auprès d’une université ou école italienne.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">2</div>
              <div class="step-item__content">
                <h4>Traduction et légalisation</h4>
                <p>Faire traduire et légaliser tous les documents nécessaires.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">3</div>
              <div class="step-item__content">
                <h4>Blocage bancaire</h4>
                <p>Bloquer 6 000€ ou fournir un garant bancaire.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">4</div>
              <div class="step-item__content">
                <h4>Demande de visa</h4>
                <p>Soumettre ta demande à l’ambassade d’Italie.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">5</div>
              <div class="step-item__content">
                <h4>Inscription et arrivée</h4>
                <p>Valider ton permis de séjour après ton arrivée en Italie.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-exclamation-triangle"></i></span> Erreurs fréquentes</h2>
          <div class="warning-box">
            <div class="warning-box__title">À éviter absolument</div>
            <ul>
              <li>Oublier de préparer un portfolio solide.</li>
              <li>Sous-estimer les frais de certains programmes.</li>
              <li>Négliger la légalisation des documents.</li>
              <li>Arriver sans assurance santé obligatoire.</li>
              <li>Choisir une école sans vérification d’accréditation.</li>
            </ul>
          </div>
        </div>
      </main>
      ''' + country_aside_template.format(country='Italie', budget_lines='          <div class="budget-line"><span class="budget-line__label">Logement</span><span class="budget-line__val">300–500€</span></div>\n          <div class="budget-line"><span class="budget-line__label">Alimentation</span><span class="budget-line__val">200–300€</span></div>\n          <div class="budget-line"><span class="budget-line__label">Transport</span><span class="budget-line__val">30–60€</span></div>\n          <div class="budget-line"><span class="budget-line__label">Loisirs</span><span class="budget-line__val">80–150€</span></div>\n          <div class="budget-line"><span class="budget-line__label">Total estimé</span><span class="budget-line__val">610–1010€</span></div>') + '''
    </div>
  </div>
</div>
<section class="section section--dark" style="text-align:center;">
  <div class="container">
    <div class="fade-up">
      <div class="tag tag--light">Prêt(e) ?</div>
      <h2 style="font-family:var(--font-display);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--cream);margin-bottom:16px;">Lance ton projet Italie dès aujourd'hui</h2>
      <p style="color:rgba(242,237,230,0.6);margin-bottom:32px;max-width:520px;margin-left:auto;margin-right:auto;">Un conseiller répond à toutes tes questions et t'aide à constituer un dossier solide pour ton projet d'études en Italie.</p>
      <a href="#" class="btn btn-whatsapp" data-wa-country="Italie"><i class="fas fa-comments"></i> Se faire accompagner sur WhatsApp</a>
    </div>
  </div>
</section>
''' + footer + '''
<script src="main.js"></script>
</body>
</html>'''

Path(root / 'italie.html').write_text(italie_html, encoding='utf-8')

# Canada page
canada_html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Étudier au Canada — Visa, Conditions, Budget | Modzi Info</title>
  <meta name="description" content="Guide complet pour étudier au Canada depuis l’Afrique : permis d’études, budget, admission et PGWP.">
  <meta name="keywords" content="étudier au Canada, visa étudiant Canada, PGWP, budget Canada, DLI">
  <link rel="canonical" href="https://modzi.info/canada">
  <link rel="stylesheet" href="styles.css">
  <link rel="icon" href="images/logo.png" type="image/png">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"Étudier au Canada : guide complet pour étudiants africains","description":"Visa, conditions d'admission et budget pour étudier au Canada","author":{{"@type":"Organization","name":"Modzi Info"}}}}</script>
</head>
<body>
{nav}
<header class="country-hero" aria-labelledby="country-title">
  <div class="country-hero__flag-bg" aria-hidden="true">🇨🇦</div>
  <div class="container">
    <nav class="breadcrumb" aria-label="Fil d'Ariane">
      <a href="index.html">Accueil</a><span>›</span>
      <a href="destinations.html">Destinations</a><span>›</span>
      <span aria-current="page">Canada</span>
    </nav>
    <div class="country-hero__tag">Destination long terme</div>
    <h1 class="country-hero__title" id="country-title">🇨🇦 Étudier au Canada</h1>
    <p class="country-hero__subtitle">Destination idéale si tu veux étudier, travailler et envisager une immigration durable.</p>
    <a href="#" class="btn btn-whatsapp" data-wa-country="Canada">
      <i class="fas fa-comments"></i> Se faire accompagner
    </a>
    <div class="country-hero__quick">
      <div class="quick-stat"><span class="quick-stat__val">8 000–20 000$/an</span><span class="quick-stat__key">Frais scolarité</span></div>
      <div class="quick-stat"><span class="quick-stat__val">1200–2000$</span><span class="quick-stat__key">Budget mensuel</span></div>
      <div class="quick-stat"><span class="quick-stat__val">6–9 mois</span><span class="quick-stat__key">Délai préparation</span></div>
      <div class="quick-stat"><span class="quick-stat__val">PGWP 3 ans</span><span class="quick-stat__key">Après diplôme</span></div>
    </div>
  </div>
</header>
<div class="country-content">
  <div class="container">
    <div class="country-layout">
      <main>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-bullseye"></i></span> Pourquoi le Canada ?</h2>
          <p>Le Canada est la destination long terme par excellence : immigration facilitée, environnement bilingue et marché du travail attractif.</p>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-user-graduate"></i></span> Profil idéal</h2>
          <p>Pour les étudiants qui veulent un projet d’études suivi d’une possibilité de travail et de résidence permanente.</p>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-clipboard"></i></span> Conditions d’admission</h2>
          <div class="info-list">
            <div class="info-item">
              <div class="info-item__icon">📄</div>
              <div class="info-item__text">
                <span class="info-item__label">Établissement reconnu</span>
                Admission dans un établissement désigné (DLI).
              </div>
            </div>
            <div class="info-item">
              <div class="info-item__icon">💰</div>
              <div class="info-item__text">
                <span class="info-item__label">Preuve de fonds</span>
                Frais de scolarité + 10 000$ pour la première année.
              </div>
            </div>
            <div class="info-item">
              <div class="info-item__icon">✅</div>
              <div class="info-item__text">
                <span class="info-item__label">Casier judiciaire</span>
                Bonne conduite et examen médical si nécessaire.
              </div>
            </div>
            <div class="info-item">
              <div class="info-item__icon">🗣️</div>
              <div class="info-item__text">
                <span class="info-item__label">Langue</span>
                IELTS/TOEFL pour l’anglais, TEF/TCF pour le français.
              </div>
            </div>
          </div>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-plane"></i></span> Procédure Visa Étudiant</h2>
          <div class="steps-list">
            <div class="step-item">
              <div class="step-item__num">1</div>
              <div class="step-item__content">
                <h4>Choisir ton établissement</h4>
                <p>Rechercher un établissement désigné (DLI) adapté à ton projet.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">2</div>
              <div class="step-item__content">
                <h4>Constituer ton dossier</h4>
                <p>Relevés de notes, diplômes, lettre de motivation, CV et recommandations.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">3</div>
              <div class="step-item__content">
                <h4>Obtenir la lettre d’admission</h4>
                <p>Sans elle, la demande de permis d’études ne peut pas avancer.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">4</div>
              <div class="step-item__content">
                <h4>Déposer la demande</h4>
                <p>Soumettre ton dossier en ligne ou via un centre désigné.</p>
              </div>
            </div>
            <div class="step-item">
              <div class="step-item__num">5</div>
              <div class="step-item__content">
                <h4>Préparer ton départ</h4>
                <p>Logement, billet, assurance santé et ouverture de compte bancaire.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="content-block fade-up">
          <h2 class="content-block__title"><span><i class="fas fa-exclamation-triangle"></i></span> Erreurs fréquentes</h2>
          <div class="warning-box">
            <div class="warning-box__title">Points de vigilance</div>
            <ul>
              <li>Ne pas vérifier que l’établissement est reconnu par Immigration Canada.</li>
              <li>Commencer les démarches trop tard.</li>
              <li>Preuve de fonds insuffisante.</li>
              <li>Lettre de motivation générique.</li>
              <li>Oublier l’assurance maladie internationale.</li>
            </ul>
          </div>
        </div>
      </main>
      ''' + country_aside_template.format(country='Canada', budget_lines='          <div class="budget-line"><span class="budget-line__label">Scolarité/an</span><span class="budget-line__val">8 000–20 000$</span></div>\n          <div class="budget-line"><span class="budget-line__label">Logement/mois</span><span class="budget-line__val">Var.</span></div>\n          <div class="budget-line"><span class="budget-line__label">Vie courante/mois</span><span class="budget-line__val">Var.</span></div>\n          <div class="budget-line"><span class="budget-line__label">Budget mensuel</span><span class="budget-line__val">1200–2000$</span></div>') + '''
    </div>
  </div>
</div>
<section class="section section--dark" style="text-align:center;">
  <div class="container">
    <div class="fade-up">
      <div class="tag tag--light">Prêt(e) ?</div>
      <h2 style="font-family:var(--font-display);font-size:clamp(2rem,4vw,3rem);font-weight:600;color:var(--cream);margin-bottom:16px;">Lance ton projet Canada dès aujourd'hui</h2>
      <p style="color:rgba(242,237,230,0.6);margin-bottom:32px;max-width:520px;margin-left:auto;margin-right:auto;">Un conseiller répond à toutes tes questions et t'aide à constituer un dossier solide pour ton projet d'études au Canada.</p>
      <a href="#" class="btn btn-whatsapp" data-wa-country="Canada"><i class="fas fa-comments"></i> Se faire accompagner sur WhatsApp</a>
    </div>
  </div>
</section>
''' + footer + '''
<script src="main.js"></script>
</body>
</html>'''

Path(root / 'canada.html').write_text(canada_html, encoding='utf-8')

print('Updated pages: destinations, france, allemagne, belgique, italie, canada')
