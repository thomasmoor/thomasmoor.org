"""All site copy, in English and French. Edit here, then run: python tools/build.py"""

from services import SERVICES, SERVICE_TEXT  # noqa: F401  (service copy lives in services.py)

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
            "intro": "Six ways I can help — from a fast, reliable website to tools that take the repetitive work off your team.",
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
        "services": SERVICE_TEXT["en"],
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
            "intro": "Six façons de vous aider — d’un site web rapide et fiable jusqu’aux outils qui libèrent votre équipe des tâches répétitives.",
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
        "services": SERVICE_TEXT["fr"],
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
