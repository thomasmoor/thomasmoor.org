"""All site copy, in English and French. Edit here, then run: python tools/build.py"""

SERVICES = [
    {"slug": "website-development", "icon": "web"},
    {"slug": "python-automation", "icon": "terminal"},
    {"slug": "technical-consulting", "icon": "chart"},
    {"slug": "ai-integration", "icon": "chip"},
]

CONTENT = {
    # ------------------------------------------------------------------ ENGLISH
    "en": {
        "lang_name": "English",
        "h1": "Thomas Moor — Digital Services",
        "h2": "Senior Consultant &amp; Business Analyst turned Digital Solutions Provider",
        "nav": {"services": "Services", "areas": "Service Areas", "about": "About", "menu": "Menu",
                "skip": "Skip to content", "main": "Main navigation"},
        "meta": {
            "home_title": "Thomas Moor — Digital Services | Websites, Python &amp; Automation",
            "home_desc": "Websites, Python tools, automation and technical consulting by Thomas Moor — 25+ years in Capital Markets, Risk and IT. Working internationally and fully remote.",
            "about_title": "About Thomas Moor | Thomas Moor — Digital Services",
            "about_desc": "Senior consultant and business analyst with 25+ years in international banking and IT (Finastra, Murex, Calypso, Reuters), now delivering web and Python services.",
            "privacy_title": "Privacy Policy | Thomas Moor — Digital Services",
            "privacy_desc": "How thomasmoor.org handles personal data, cookies and analytics.",
        },
        "hero": {
            "title": "Digital Solutions Provider",
            "lead": "Websites, Python tools and automation — delivered with the rigour of 25 years in banking IT.",
            "cta1": "Explore services",
        },
        "form": {
            "title": "Tell me about your project",
            "intro": "I usually reply within one business day.",
            "name": "Name", "phone": "Phone", "email": "eMail", "service": "Service",
            "service_ph": "Select a service", "when": "When do you need it?", "when_ph": "Select a timeframe",
            "when_opts": [("Emergency", "Emergency"), ("This week", "This week"), ("This month", "This month")],
            "message": "Message", "message_ph": "A few words about what you need…",
            "submit": "Send request", "required": "required",
            "note": "Your details are only used to answer your request. See the <a href=\"{privacy}\">privacy policy</a>.",
            "subject": "New enquiry from thomasmoor.org",
            "msg": {
                "required": "Please enter your name.",
                "email": "Please enter a valid email address.",
                "sending": "Sending…",
                "success": "Thank you! Your message has been sent. I will get back to you shortly.",
                "error": "Sorry, the message could not be sent. Please email contact@thomasmoor.org.",
                "notConfigured": "The form is not active yet. Please email contact@thomasmoor.org.",
            },
        },
        "services_section": {
            "kicker": "What I do", "title": "Services",
            "intro": "Four ways I can help — from a fast, reliable website to tools that take the repetitive work off your team.",
            "more": "Learn more",
        },
        "areas": {
            "kicker": "Where I work", "title": "Service Areas",
            "text": "I work <strong>internationally and fully remotely</strong>. Whether you are in Europe, the Middle East, or elsewhere, distance has <strong>no effect on the quality of the work or the communication</strong>. I maintain the same high standards of delivery, responsiveness, and collaboration as if I were on-site. All projects are managed with clear timelines, regular updates, and structured documentation.",
            "regions": ["Europe", "Middle East", "Worldwide"],
            "features": [
                ("clock", "Clear timelines", "A written plan with milestones and dates, agreed before work starts."),
                ("message", "Regular updates", "Progress reports at a rhythm that suits you — no chasing needed."),
                ("doc", "Structured documentation", "Specs, decisions and handover notes, kept in one place."),
            ],
        },
        "about_section": {
            "kicker": "About", "title": "Rigour from banking, applied to your project",
            "more": "More about me",
            "stats": [("25+", "years in banking &amp; IT"), ("2", "languages: FR / EN"), ("100%", "remote delivery")],
        },
        "about": [
            "With over 25 years of experience in international banking and IT — including senior roles at Finastra, Murex, Calypso, and Reuters — I have spent my career solving complex technical and business problems. Today, I apply that same rigor, precision, and project discipline to web services and Python development.",
            "I combine deep technical skills (SQL, Python, Java, VBA, JavaScript) with a consultant’s mindset: I listen, I spec, I deliver. Whether you need a clean, simple website or a custom automation tool, I bring the same commitment to quality, clear communication, and on-time delivery that I have brought to tier-one financial institutions across Europe and the Middle East.",
            "I am bilingual (French/English), detail-oriented, and comfortable working with clients anywhere in the world.",
        ],
        "about_page": {
            "glance": "At a glance",
            "rows": [
                ("Experience", "25+ years in Capital Markets, Risk and IT"),
                ("Previous roles", "Senior roles at Finastra, Murex, Calypso and Reuters"),
                ("Technical skills", "SQL, Python, Java, VBA, JavaScript, HTML/CSS"),
                ("Languages", "French, English"),
                ("Clients", "Europe, the Middle East and worldwide — fully remote"),
            ],
            "approach_title": "How I work",
            "approach": [
                ("I listen", "We start with your goals, your constraints and your users — not with technology."),
                ("I spec", "You receive a short written specification, a timeline and a fixed scope."),
                ("I deliver", "Regular updates, tested work and clear documentation at handover."),
            ],
        },
        "service_page": {
            "breadcrumb_home": "Home", "breadcrumb_services": "Services",
            "why": "Why it matters", "expect": "What you can expect",
            "others": "Other services",
            "cta_title": "Ready to discuss your project?",
            "cta_text": "Tell me what you need — you will get a clear answer, a plan and a quote.",
            "cta_btn": "Request a quote",
        },
        "services": {
            "website-development": {
                "name": "Website Development &amp; Delivery",
                "short": "Design, build, and deployment of simple, fast, and reliable HTML/CSS websites (including GitHub Pages hosting).",
                "intro": [
                    "A website is often the first conversation a client has with your business. I design and build clean, hand-coded HTML/CSS websites that load fast, read well on every screen and are easy to keep up to date. No heavy page builders and no plugin sprawl — just a solid, well-structured site that you fully own.",
                    "From the first sketch to the moment your domain goes live, I take care of the whole chain: structure and content, design, development, testing and deployment — including free, secure hosting on GitHub Pages with your own domain name.",
                ],
                "why": [
                    "Speed and reliability are not luxuries. Visitors leave slow sites within seconds, search engines favour fast pages, and every extra plugin is one more thing that can break or be attacked. A simple static website removes most of those risks: there is no database to hack, nothing to patch every week, and hosting costs can drop to zero.",
                    "For consultants, small businesses and independent professionals, that means a credible online presence that simply works — and keeps working without an expensive maintenance contract.",
                ],
                "expect": [
                    "A short discovery call and a one-page written spec before any work starts",
                    "A responsive design that works on phones, tablets and desktops",
                    "Clean, standards-based HTML/CSS with on-page SEO basics (titles, descriptions, sitemap)",
                    "Contact form, analytics and GDPR-aware cookie consent, set up for you",
                    "Deployment on GitHub Pages (or your own hosting) with your domain and HTTPS",
                    "Handover notes so you know exactly how to update your content",
                ],
            },
            "python-automation": {
                "name": "Advanced Python Tool Development and Automation",
                "short": "Custom scripting, data processing, and integration tools for business workflows.",
                "intro": [
                    "Many businesses still run on spreadsheets, copy-paste and manual exports. I build custom Python tools that take over that work: scripts that collect and clean data, generate reports, move information between systems or check results automatically.",
                    "Each tool is designed around your actual workflow — readable, documented, and robust enough to run unattended every day.",
                ],
                "why": [
                    "Manual, repetitive processing is slow, expensive and error-prone. One wrong formula or one missed file can quietly corrupt a report that people rely on. Automating these steps frees your team for higher-value work and makes results consistent and auditable.",
                    "Years in capital markets, where data quality is non-negotiable, taught me a simple discipline that I apply to every tool: validate the inputs, log what happens, and fail loudly rather than silently.",
                ],
                "expect": [
                    "Analysis of your current process and a clear spec of what the tool will do",
                    "Data processing with pandas, SQL databases, Excel/CSV files and APIs",
                    "Integrations between the systems you already use",
                    "Scheduled or on-demand execution, with logging and error alerts",
                    "Tested, documented code that you own",
                    "Support after delivery, and evolutions as your needs grow",
                ],
            },
            "technical-consulting": {
                "name": "Technical Consulting &amp; Business Analysis",
                "short": "Bridging business needs and technical implementation (25+ years in Capital Markets, Risk, and IT).",
                "intro": [
                    "Projects rarely fail because of technology alone. They fail when business needs and technical implementation drift apart. As a consultant and business analyst, I sit between the two: I understand what your teams need, translate it into precise requirements, and make sure that what gets built actually matches.",
                    "With 25+ years in Capital Markets, Risk and IT — including senior roles at Finastra, Murex, Calypso and Reuters — I have worked on trading, risk and back-office systems for tier-one banks across Europe and the Middle East.",
                ],
                "why": [
                    "Unclear requirements are the most expensive bug in any project. Every misunderstanding discovered late costs time, budget and trust. A structured analysis up front — led by someone who speaks both the business and the technical language — keeps a project on scope, on time and on budget.",
                    "An experienced outside view also helps you challenge vendor proposals, prioritise what really matters and avoid paying for features nobody will use.",
                ],
                "expect": [
                    "Workshops with stakeholders to capture needs and constraints",
                    "Functional and technical specifications, user stories and acceptance criteria",
                    "Gap analysis, process mapping and solution assessment",
                    "Data analysis and SQL investigation to support decisions",
                    "Test strategy, UAT coordination and go-live support",
                    "Clear, regular reporting to management",
                ],
            },
            "ai-integration": {
                "name": "Automation &amp; AI Integration",
                "short": "Streamlining content creation, reporting, and repetitive tasks using Python and JavaScript.",
                "intro": [
                    "Automation and artificial intelligence are now practical tools for small teams, not just for large corporations. I help you put them to work on concrete tasks: drafting and reformatting content, summarising documents, producing recurring reports and handling the repetitive steps in between.",
                    "I build these workflows with Python and JavaScript, connecting AI services to the tools you already use, so the results land where you need them — with a human check where it matters.",
                ],
                "why": [
                    "Time spent on repetitive writing, formatting and reporting is time not spent with clients. A well-designed automation can turn hours of work into minutes.",
                    "Used carelessly, however, AI produces errors and creates risks. The value comes from a well-scoped workflow with clear rules, validation steps and human oversight — which is exactly how I design them.",
                ],
                "expect": [
                    "Identification of the tasks where automation brings a real return",
                    "AI-assisted content creation and reporting pipelines",
                    "Integration with your tools: email, spreadsheets, CMS and APIs",
                    "Guardrails: review steps, validation and data-privacy safeguards",
                    "Documentation and a hand-over session so your team stays in control",
                    "Measured results: time saved and quality gained",
                ],
            },
        },
        "footer": {
            "services": "Services", "info": "Information", "about": "About",
            "privacy": "Privacy policy", "cookies": "Cookie settings", "rights": "All rights reserved.",
            "other_lang": "Version française",
        },
        "cookie": {
            "label": "Cookie consent",
            "text": "This site uses cookies for anonymous audience measurement (Google Analytics), only if you agree.",
            "more": "Privacy policy", "accept": "Accept", "decline": "Decline",
        },
        "privacy": {
            "title": "Privacy Policy",
            "updated": "Last updated: 10 November 2026",
            "sections": [
                ("Who is responsible", [
                    "This website, thomasmoor.org, is operated by <strong>Thomas Moor Consulting</strong> (“I”, “me”), which is the data controller for the personal data described below.",
                    "For any question about your data, write to <a href=\"mailto:contact@thomasmoor.org\">contact@thomasmoor.org</a>.",
                ]),
                ("Contact form", [
                    "When you use the contact form, I receive the information you enter: your name and, if you provide them, your phone number, email address, the service you are interested in, your timeframe and your message.",
                    "This data is used only to answer your request and, if we work together, to prepare and manage our collaboration. The legal basis is the steps taken at your request before entering into a contract, and my legitimate interest in answering enquiries.",
                    "Form messages are transmitted by <strong>Web3Forms</strong>, a form-delivery service that forwards them to my mailbox. I keep enquiries for up to three years after our last contact, unless a contract requires a longer retention period.",
                ]),
                ("Analytics and cookies", [
                    "With your consent only, this site uses <strong>Google Analytics 4</strong> (Google Ireland Ltd.) to measure audience anonymously: pages visited, approximate location, device type and how you arrived on the site. Google Analytics 4 does not log or store IP addresses.",
                    "Google Analytics sets the cookies <code>_ga</code> and <code>_ga_&lt;ID&gt;</code>, which last up to two years. They are not set if you decline. The legal basis is your consent, which you can withdraw at any time using the “Cookie settings” link at the bottom of every page.",
                    "Your choice itself is stored in your browser (local storage entry <code>tm_consent</code>). It contains no personal data.",
                ]),
                ("Hosting and third-party services", [
                    "The site is hosted on <strong>GitHub Pages</strong> (GitHub, Inc.), which may record technical data such as your IP address in server logs for security purposes. Fonts are served by <strong>Google Fonts</strong>, which receives your IP address when the page loads.",
                    "Some of these providers are located outside the European Union. Transfers are covered by the EU–US Data Privacy Framework and/or the European Commission’s Standard Contractual Clauses.",
                ]),
                ("Your rights", [
                    "Under the GDPR you have the right to access, correct and delete your data, to restrict or object to its processing, to data portability, and to withdraw your consent at any time. To exercise these rights, email <a href=\"mailto:contact@thomasmoor.org\">contact@thomasmoor.org</a>.",
                    "You also have the right to lodge a complaint with a data-protection supervisory authority, for example the CNIL in France or the authority of your country of residence.",
                ]),
                ("Changes", [
                    "This policy may be updated when the site or the services it uses change. The date at the top of this page shows the latest version.",
                ]),
            ],
        },
        "notfound": {"title": "Page not found", "text": "The page you are looking for does not exist or has moved.", "btn": "Back to home"},
    },

    # ------------------------------------------------------------------ FRENCH
    "fr": {
        "lang_name": "Français",
        "h1": "Thomas Moor — Services numériques",
        "h2": "Consultant senior &amp; Business Analyst devenu fournisseur de solutions numériques",
        "nav": {"services": "Services", "areas": "Zones d’intervention", "about": "À propos", "menu": "Menu",
                "skip": "Aller au contenu", "main": "Navigation principale"},
        "meta": {
            "home_title": "Thomas Moor — Services numériques | Sites web, Python &amp; automatisation",
            "home_desc": "Sites web, outils Python, automatisation et conseil technique par Thomas Moor — plus de 25 ans en marchés de capitaux, risques et IT. À l’international et entièrement à distance.",
            "about_title": "À propos de Thomas Moor | Thomas Moor — Services numériques",
            "about_desc": "Consultant senior et business analyst, plus de 25 ans dans la banque internationale et l’IT (Finastra, Murex, Calypso, Reuters), désormais au service de vos projets web et Python.",
            "privacy_title": "Politique de confidentialité | Thomas Moor — Services numériques",
            "privacy_desc": "Comment thomasmoor.org traite les données personnelles, les cookies et la mesure d’audience.",
        },
        "hero": {
            "title": "Fournisseur de solutions numériques",
            "lead": "Sites web, outils Python et automatisation — livrés avec la rigueur de 25 ans d’informatique bancaire.",
            "cta1": "Découvrir les services",
        },
        "form": {
            "title": "Parlez-moi de votre projet",
            "intro": "Je réponds généralement sous un jour ouvré.",
            "name": "Nom", "phone": "Téléphone", "email": "E-mail", "service": "Service",
            "service_ph": "Choisissez un service", "when": "Pour quand en avez-vous besoin ?", "when_ph": "Choisissez un délai",
            "when_opts": [("Emergency", "Urgent"), ("This week", "Cette semaine"), ("This month", "Ce mois-ci")],
            "message": "Message", "message_ph": "Quelques mots sur votre besoin…",
            "submit": "Envoyer la demande", "required": "obligatoire",
            "note": "Vos coordonnées servent uniquement à répondre à votre demande. Voir la <a href=\"{privacy}\">politique de confidentialité</a>.",
            "subject": "Nouvelle demande depuis thomasmoor.org (FR)",
            "msg": {
                "required": "Veuillez indiquer votre nom.",
                "email": "Veuillez saisir une adresse e-mail valide.",
                "sending": "Envoi en cours…",
                "success": "Merci ! Votre message a bien été envoyé. Je vous réponds très vite.",
                "error": "Désolé, le message n’a pas pu être envoyé. Écrivez-moi à contact@thomasmoor.org.",
                "notConfigured": "Le formulaire n’est pas encore actif. Écrivez-moi à contact@thomasmoor.org.",
            },
        },
        "services_section": {
            "kicker": "Ce que je fais", "title": "Services",
            "intro": "Quatre façons de vous aider — d’un site web rapide et fiable jusqu’aux outils qui libèrent votre équipe des tâches répétitives.",
            "more": "En savoir plus",
        },
        "areas": {
            "kicker": "Où j’interviens", "title": "Zones d’intervention",
            "text": "Je travaille <strong>à l’international et entièrement à distance</strong>. Que vous soyez en Europe, au Moyen-Orient ou ailleurs, la distance <strong>n’a aucun effet sur la qualité du travail ni sur la communication</strong>. Je maintiens les mêmes exigences de livraison, de réactivité et de collaboration que si j’étais sur site. Tous les projets sont gérés avec des délais clairs, des points d’avancement réguliers et une documentation structurée.",
            "regions": ["Europe", "Moyen-Orient", "Monde entier"],
            "features": [
                ("clock", "Des délais clairs", "Un planning écrit, avec jalons et dates, validé avant le démarrage."),
                ("message", "Des points réguliers", "Des comptes rendus au rythme qui vous convient — sans avoir à relancer."),
                ("doc", "Une documentation structurée", "Spécifications, décisions et notes de passation, réunies au même endroit."),
            ],
        },
        "about_section": {
            "kicker": "À propos", "title": "La rigueur de la banque, au service de votre projet",
            "more": "En savoir plus sur moi",
            "stats": [("25+", "ans en banque &amp; IT"), ("2", "langues : FR / EN"), ("100 %", "à distance")],
        },
        "about": [
            "Fort de plus de 25 ans d’expérience dans la banque internationale et l’informatique — notamment à des postes seniors chez Finastra, Murex, Calypso et Reuters — j’ai consacré ma carrière à résoudre des problèmes techniques et métier complexes. Aujourd’hui, j’applique cette même rigueur, cette même précision et cette même discipline de gestion de projet aux services web et au développement Python.",
            "J’associe de solides compétences techniques (SQL, Python, Java, VBA, JavaScript) à un état d’esprit de consultant : j’écoute, je spécifie, je livre. Qu’il vous faille un site web simple et soigné ou un outil d’automatisation sur mesure, j’apporte le même engagement envers la qualité, la clarté de la communication et le respect des délais que celui dont j’ai fait preuve auprès de grandes institutions financières en Europe et au Moyen-Orient.",
            "Bilingue (français/anglais) et attentif aux détails, je travaille sans difficulté avec des clients du monde entier.",
        ],
        "about_page": {
            "glance": "En bref",
            "rows": [
                ("Expérience", "Plus de 25 ans en marchés de capitaux, risques et IT"),
                ("Parcours", "Postes seniors chez Finastra, Murex, Calypso et Reuters"),
                ("Compétences", "SQL, Python, Java, VBA, JavaScript, HTML/CSS"),
                ("Langues", "Français, anglais"),
                ("Clients", "Europe, Moyen-Orient et monde entier — 100 % à distance"),
            ],
            "approach_title": "Ma méthode",
            "approach": [
                ("J’écoute", "Nous partons de vos objectifs, de vos contraintes et de vos utilisateurs — pas de la technologie."),
                ("Je spécifie", "Vous recevez une courte spécification écrite, un planning et un périmètre défini."),
                ("Je livre", "Des points réguliers, un travail testé et une documentation claire à la livraison."),
            ],
        },
        "service_page": {
            "breadcrumb_home": "Accueil", "breadcrumb_services": "Services",
            "why": "Pourquoi c’est important", "expect": "Ce que vous pouvez attendre",
            "others": "Autres services",
            "cta_title": "Prêt à parler de votre projet ?",
            "cta_text": "Décrivez votre besoin — vous recevrez une réponse claire, un plan et un devis.",
            "cta_btn": "Demander un devis",
        },
        "services": {
            "website-development": {
                "name": "Création &amp; mise en ligne de sites web",
                "short": "Conception, développement et mise en ligne de sites HTML/CSS simples, rapides et fiables (hébergement GitHub Pages inclus).",
                "intro": [
                    "Votre site web est souvent le premier échange entre un client et votre activité. Je conçois et développe des sites HTML/CSS codés à la main, propres, rapides, lisibles sur tous les écrans et faciles à mettre à jour. Pas de constructeur de pages lourd ni d’empilement d’extensions : un site solide, bien structuré, dont vous êtes entièrement propriétaire.",
                    "De la première esquisse à la mise en ligne sur votre nom de domaine, je prends en charge toute la chaîne : structure et contenus, design, développement, tests et déploiement — y compris un hébergement gratuit et sécurisé sur GitHub Pages avec votre propre domaine.",
                ],
                "why": [
                    "La rapidité et la fiabilité ne sont pas un luxe. Les visiteurs quittent un site lent en quelques secondes, les moteurs de recherche privilégient les pages rapides, et chaque extension supplémentaire est un point de panne ou d’attaque de plus. Un site statique simple élimine la plupart de ces risques : pas de base de données à pirater, rien à corriger chaque semaine, et des frais d’hébergement qui peuvent tomber à zéro.",
                    "Pour un consultant, une petite entreprise ou un indépendant, c’est une présence en ligne crédible qui fonctionne, tout simplement — et qui continue de fonctionner sans contrat de maintenance coûteux.",
                ],
                "expect": [
                    "Un court échange de cadrage et une spécification écrite d’une page avant tout démarrage",
                    "Un design responsive, adapté aux mobiles, tablettes et ordinateurs",
                    "Un code HTML/CSS propre et conforme aux standards, avec les bases du SEO (titres, descriptions, plan du site)",
                    "Formulaire de contact, mesure d’audience et bandeau cookies conforme au RGPD, configurés pour vous",
                    "Mise en ligne sur GitHub Pages (ou votre hébergement) avec votre domaine et le HTTPS",
                    "Des notes de passation pour savoir exactement comment mettre à jour vos contenus",
                ],
            },
            "python-automation": {
                "name": "Développement d’outils Python avancés et automatisation",
                "short": "Scripts sur mesure, traitement de données et outils d’intégration pour vos processus métier.",
                "intro": [
                    "Beaucoup d’entreprises fonctionnent encore à coups de tableurs, de copier-coller et d’exports manuels. Je développe des outils Python sur mesure qui prennent ce travail en charge : scripts qui collectent et nettoient les données, génèrent des rapports, transfèrent l’information entre systèmes ou contrôlent automatiquement les résultats.",
                    "Chaque outil est conçu autour de votre processus réel — lisible, documenté et assez robuste pour tourner chaque jour sans surveillance.",
                ],
                "why": [
                    "Les traitements manuels et répétitifs sont lents, coûteux et sources d’erreurs. Une formule erronée ou un fichier oublié peut fausser discrètement un rapport sur lequel tout le monde s’appuie. Automatiser ces étapes libère votre équipe pour un travail à plus forte valeur et rend les résultats cohérents et vérifiables.",
                    "Des années sur les marchés de capitaux, où la qualité des données n’est pas négociable, m’ont appris une discipline simple que j’applique à chaque outil : valider les entrées, tracer ce qui se passe, et signaler clairement une erreur plutôt que l’ignorer.",
                ],
                "expect": [
                    "Une analyse de votre processus actuel et une spécification claire de ce que fera l’outil",
                    "Traitement de données avec pandas, bases SQL, fichiers Excel/CSV et API",
                    "Des intégrations entre les systèmes que vous utilisez déjà",
                    "Exécution planifiée ou à la demande, avec journalisation et alertes d’erreur",
                    "Un code testé et documenté, qui vous appartient",
                    "Un support après livraison et des évolutions au rythme de vos besoins",
                ],
            },
            "technical-consulting": {
                "name": "Conseil technique &amp; analyse métier",
                "short": "Faire le lien entre les besoins métier et la mise en œuvre technique (plus de 25 ans en marchés de capitaux, risques et IT).",
                "intro": [
                    "Un projet échoue rarement à cause de la seule technologie. Il échoue quand les besoins métier et la mise en œuvre technique s’éloignent l’un de l’autre. En tant que consultant et business analyst, je me place entre les deux : je comprends ce dont vos équipes ont besoin, je le traduis en exigences précises et je m’assure que ce qui est construit y correspond vraiment.",
                    "Avec plus de 25 ans en marchés de capitaux, risques et IT — notamment à des postes seniors chez Finastra, Murex, Calypso et Reuters — j’ai travaillé sur des systèmes de trading, de risque et de back-office pour de grandes banques en Europe et au Moyen-Orient.",
                ],
                "why": [
                    "Des exigences floues sont le bug le plus coûteux d’un projet. Chaque malentendu découvert tardivement coûte du temps, du budget et de la confiance. Une analyse structurée en amont — menée par quelqu’un qui parle à la fois le langage du métier et celui de la technique — permet de tenir le périmètre, les délais et le budget.",
                    "Un regard extérieur expérimenté vous aide aussi à challenger les propositions des éditeurs, à prioriser l’essentiel et à éviter de payer des fonctionnalités que personne n’utilisera.",
                ],
                "expect": [
                    "Des ateliers avec les parties prenantes pour recueillir besoins et contraintes",
                    "Spécifications fonctionnelles et techniques, user stories et critères d’acceptation",
                    "Analyse d’écarts, cartographie des processus et évaluation de solutions",
                    "Analyses de données et requêtes SQL pour éclairer les décisions",
                    "Stratégie de test, coordination de la recette (UAT) et accompagnement à la mise en production",
                    "Un reporting clair et régulier auprès de la direction",
                ],
            },
            "ai-integration": {
                "name": "Automatisation &amp; intégration de l’IA",
                "short": "Automatiser la création de contenu, le reporting et les tâches répétitives avec Python et JavaScript.",
                "intro": [
                    "L’automatisation et l’intelligence artificielle sont aujourd’hui des outils concrets pour les petites équipes, pas seulement pour les grands groupes. Je vous aide à les mettre au service de tâches précises : rédaction et mise en forme de contenus, synthèse de documents, rapports récurrents et toutes les étapes répétitives entre les deux.",
                    "Je construis ces flux en Python et JavaScript, en connectant les services d’IA aux outils que vous utilisez déjà, pour que les résultats arrivent là où vous en avez besoin — avec une validation humaine quand c’est nécessaire.",
                ],
                "why": [
                    "Le temps passé à rédiger, mettre en forme et produire des rapports répétitifs est du temps en moins pour vos clients. Une automatisation bien conçue peut transformer des heures de travail en quelques minutes.",
                    "Utilisée sans précaution, l’IA produit pourtant des erreurs et crée des risques. La valeur vient d’un flux bien cadré, avec des règles claires, des étapes de contrôle et une supervision humaine — c’est exactement ainsi que je les conçois.",
                ],
                "expect": [
                    "L’identification des tâches où l’automatisation apporte un vrai retour",
                    "Des chaînes de création de contenu et de reporting assistées par l’IA",
                    "L’intégration à vos outils : e-mail, tableurs, CMS et API",
                    "Des garde-fous : étapes de relecture, contrôles et protection des données",
                    "Documentation et séance de prise en main pour que votre équipe garde la main",
                    "Des résultats mesurés : temps gagné et qualité améliorée",
                ],
            },
        },
        "footer": {
            "services": "Services", "info": "Informations", "about": "À propos",
            "privacy": "Politique de confidentialité", "cookies": "Gérer les cookies", "rights": "Tous droits réservés.",
            "other_lang": "English version",
        },
        "cookie": {
            "label": "Consentement aux cookies",
            "text": "Ce site utilise des cookies de mesure d’audience anonyme (Google Analytics), uniquement si vous l’acceptez.",
            "more": "Politique de confidentialité", "accept": "Accepter", "decline": "Refuser",
        },
        "privacy": {
            "title": "Politique de confidentialité",
            "updated": "Dernière mise à jour : 10 novembre 2026",
            "sections": [
                ("Responsable du traitement", [
                    "Le site thomasmoor.org est édité par <strong>Thomas Moor Consulting</strong> (« je »), responsable du traitement des données personnelles décrites ci-dessous.",
                    "Pour toute question sur vos données, écrivez à <a href=\"mailto:contact@thomasmoor.org\">contact@thomasmoor.org</a>.",
                ]),
                ("Formulaire de contact", [
                    "Lorsque vous utilisez le formulaire de contact, je reçois les informations que vous saisissez : votre nom et, si vous les indiquez, votre numéro de téléphone, votre adresse e-mail, le service qui vous intéresse, votre délai et votre message.",
                    "Ces données servent uniquement à répondre à votre demande et, si nous travaillons ensemble, à préparer et gérer notre collaboration. La base légale est l’exécution de mesures précontractuelles prises à votre demande et mon intérêt légitime à répondre aux sollicitations.",
                    "Les messages sont transmis par <strong>Web3Forms</strong>, un service d’acheminement de formulaires qui les transfère vers ma messagerie. Je conserve les demandes jusqu’à trois ans après notre dernier échange, sauf si un contrat impose une durée plus longue.",
                ]),
                ("Mesure d’audience et cookies", [
                    "Uniquement avec votre accord, ce site utilise <strong>Google Analytics 4</strong> (Google Ireland Ltd.) pour mesurer l’audience de façon anonyme : pages consultées, localisation approximative, type d’appareil et provenance des visites. Google Analytics 4 n’enregistre ni ne conserve les adresses IP.",
                    "Google Analytics dépose les cookies <code>_ga</code> et <code>_ga_&lt;ID&gt;</code>, d’une durée maximale de deux ans. Ils ne sont pas déposés si vous refusez. La base légale est votre consentement, que vous pouvez retirer à tout moment via le lien « Gérer les cookies » en bas de chaque page.",
                    "Votre choix est lui-même enregistré dans votre navigateur (entrée de stockage local <code>tm_consent</code>). Il ne contient aucune donnée personnelle.",
                ]),
                ("Hébergement et services tiers", [
                    "Le site est hébergé par <strong>GitHub Pages</strong> (GitHub, Inc.), qui peut enregistrer des données techniques comme votre adresse IP dans ses journaux serveur à des fins de sécurité. Les polices de caractères sont fournies par <strong>Google Fonts</strong>, qui reçoit votre adresse IP au chargement de la page.",
                    "Certains de ces prestataires sont situés hors de l’Union européenne. Ces transferts sont encadrés par le Data Privacy Framework UE–États-Unis et/ou les clauses contractuelles types de la Commission européenne.",
                ]),
                ("Vos droits", [
                    "Conformément au RGPD, vous disposez d’un droit d’accès, de rectification et d’effacement de vos données, d’un droit à la limitation et d’opposition au traitement, d’un droit à la portabilité et du droit de retirer votre consentement à tout moment. Pour les exercer, écrivez à <a href=\"mailto:contact@thomasmoor.org\">contact@thomasmoor.org</a>.",
                    "Vous pouvez également introduire une réclamation auprès d’une autorité de protection des données, par exemple la CNIL en France ou l’autorité de votre pays de résidence.",
                ]),
                ("Modifications", [
                    "Cette politique peut être mise à jour lorsque le site ou les services qu’il utilise évoluent. La date en haut de cette page indique la version en vigueur.",
                ]),
            ],
        },
        "notfound": {"title": "Page introuvable", "text": "La page que vous cherchez n’existe pas ou a été déplacée.", "btn": "Retour à l’accueil"},
    },
}
