"""Service list and service-page copy (EN + FR). The order here is the order on the site."""

SERVICES = [
    {"slug": "website-development", "icon": "web"},
    {"slug": "python-development", "icon": "terminal"},
    {"slug": "automation", "icon": "cycle"},
    {"slug": "technical-consulting", "icon": "chart"},
    {"slug": "business-analysis", "icon": "clipboard"},
    {"slug": "ai-integration", "icon": "sparkle"},
]

SERVICE_TEXT = {
    # ------------------------------------------------------------------ ENGLISH
    "en": {
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
        "python-development": {
            "name": "Advanced Python Tool Development",
            "short": "Custom Python scripting, data processing, and integration tools built around your business workflows.",
            "intro": [
                "Many businesses still depend on spreadsheets, copy-paste and fragile one-off scripts. I design and build robust Python tools tailored to the way you work: data-processing engines, connectors between systems, command-line utilities, small internal web apps and APIs.",
                "Each tool is readable, documented and tested — written to be maintained, not just to work once.",
            ],
            "why": [
                "Off-the-shelf software rarely fits a specific workflow perfectly. A well-built custom tool closes that gap: it does exactly what you need, integrates with the systems you already have and grows with your business.",
                "Years in capital markets, where data quality is non-negotiable, taught me a simple discipline that I apply to every tool: validate the inputs, log what happens, and fail loudly rather than silently.",
            ],
            "expect": [
                "A clear spec of what the tool will do, agreed before development starts",
                "Data processing with pandas, SQL databases, Excel/CSV files and APIs",
                "Connectors and integrations between the systems you already use",
                "Clean, tested and documented code that you fully own",
                "Packaging and deployment on your machines, server or cloud",
                "Support after delivery, and evolutions as your needs grow",
            ],
        },
        "automation": {
            "name": "Automation",
            "short": "Automating reporting, data handling, and repetitive tasks with Python and JavaScript — so your team can focus on higher-value work.",
            "intro": [
                "Every business has tasks that are done by hand, over and over: downloading files, updating spreadsheets, copying data between applications, producing the same weekly report. I automate these workflows end to end with Python and JavaScript.",
                "The result runs on a schedule or at the click of a button, with clear logs and alerts — and with a human check wherever it matters.",
            ],
            "why": [
                "Manual, repetitive work is slow, expensive and error-prone. One wrong formula or one missed file can quietly corrupt a report that people rely on. Automation makes these processes faster, consistent and auditable.",
                "It also frees skilled people from low-value tasks. A few hours saved every week quickly add up to days of extra capacity every month.",
            ],
            "expect": [
                "A review of your current processes to find where automation pays off most",
                "Automated reports, file handling and data transfers between applications",
                "Spreadsheet and Excel/VBA automation, browser and web automation",
                "Scheduled or on-demand execution, with logging and error alerts",
                "Documentation so your team understands and controls every step",
                "Measured results: time saved and errors avoided",
            ],
        },
        "technical-consulting": {
            "name": "Technical Consulting",
            "short": "Independent technical expertise on systems, architecture, and implementation — backed by 25+ years in Capital Markets, Risk, and IT.",
            "intro": [
                "Choosing, implementing or modernising a system involves decisions that are hard to reverse. I provide independent, hands-on technical advice to help you make them with confidence: assessing the options, designing the solution and guiding the implementation.",
                "With 25+ years in Capital Markets, Risk and IT — including senior roles at Finastra, Murex, Calypso and Reuters — I have worked on trading, risk and back-office platforms for tier-one banks across Europe and the Middle East.",
            ],
            "why": [
                "Technology choices shape costs, risks and agility for years. An experienced outside view helps you challenge vendor proposals, avoid over-engineering and focus the budget on what really matters.",
                "Having worked on both the vendor and the client side, I know where projects usually go wrong — and how to prevent it.",
            ],
            "expect": [
                "Assessment of your current systems, architecture and data flows",
                "Solution design and technology recommendations",
                "Vendor and package evaluation, including trading and risk platforms",
                "Implementation planning, migration strategy and risk review",
                "Hands-on support on integration, data and SQL questions",
                "Clear, regular reporting to management",
            ],
        },
        "business-analysis": {
            "name": "Business Analysis",
            "short": "Bridging business needs and technical implementation with clear requirements, specifications, and process analysis.",
            "intro": [
                "Projects rarely fail because of technology alone. They fail when business needs and technical implementation drift apart. As a business analyst, I sit between the two: I understand what your teams need, translate it into precise requirements, and make sure that what gets built actually matches.",
                "I listen, I spec, I deliver: structured workshops, clear documentation and close follow-up from the first meeting to go-live.",
            ],
            "why": [
                "Unclear requirements are the most expensive bug in any project. Every misunderstanding discovered late costs time, budget and trust.",
                "A structured analysis up front — led by someone who speaks both the business and the technical language — keeps a project on scope, on time and on budget.",
            ],
            "expect": [
                "Workshops with stakeholders to capture needs and constraints",
                "Functional specifications, user stories and acceptance criteria",
                "Process mapping and gap analysis between current and target state",
                "Data analysis and SQL investigation to support decisions",
                "Test strategy, UAT coordination and go-live support",
                "Documentation that stays useful after the project ends",
            ],
        },
        "ai-integration": {
            "name": "AI Integration",
            "short": "Putting AI to work on content creation, document processing, and reporting — with the right guardrails.",
            "intro": [
                "Artificial intelligence is now a practical tool for small teams, not just for large corporations. I help you put it to work on concrete tasks: drafting and reformatting content, summarising documents and extracting information from them, sorting incoming requests and producing recurring reports.",
                "I integrate AI services into the tools you already use with Python and JavaScript, so the results land where you need them — with a human check where it matters.",
            ],
            "why": [
                "Used well, AI can turn hours of reading, writing and formatting into minutes.",
                "Used carelessly, it produces errors and creates risks for your data and your reputation. The value comes from a well-scoped workflow with clear rules, validation steps and human oversight — which is exactly how I design them.",
            ],
            "expect": [
                "Identification of the use cases where AI brings a real return",
                "AI-assisted content creation and document-processing pipelines",
                "Integration with your tools: email, spreadsheets, CMS and APIs",
                "Guardrails: review steps, validation and data-privacy safeguards",
                "Documentation and a hand-over session so your team stays in control",
                "Measured results: time saved and quality gained",
            ],
        },
    },

    # ------------------------------------------------------------------ FRENCH
    "fr": {
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
        "python-development": {
            "name": "Développement d’outils Python avancés",
            "short": "Scripts Python sur mesure, traitement de données et outils d’intégration, conçus autour de vos processus métier.",
            "intro": [
                "Beaucoup d’entreprises dépendent encore de tableurs, de copier-coller et de scripts ponctuels fragiles. Je conçois et développe des outils Python robustes, adaptés à votre façon de travailler : moteurs de traitement de données, connecteurs entre systèmes, utilitaires en ligne de commande, petites applications web internes et API.",
                "Chaque outil est lisible, documenté et testé — écrit pour être maintenu, pas seulement pour fonctionner une fois.",
            ],
            "why": [
                "Un logiciel standard correspond rarement parfaitement à un processus spécifique. Un outil sur mesure bien conçu comble cet écart : il fait exactement ce dont vous avez besoin, s’intègre aux systèmes que vous utilisez déjà et évolue avec votre activité.",
                "Des années sur les marchés de capitaux, où la qualité des données n’est pas négociable, m’ont appris une discipline simple que j’applique à chaque outil : valider les entrées, tracer ce qui se passe, et signaler clairement une erreur plutôt que l’ignorer.",
            ],
            "expect": [
                "Une spécification claire de ce que fera l’outil, validée avant le développement",
                "Traitement de données avec pandas, bases SQL, fichiers Excel/CSV et API",
                "Des connecteurs et intégrations entre les systèmes que vous utilisez déjà",
                "Un code propre, testé et documenté, dont vous êtes entièrement propriétaire",
                "Packaging et déploiement sur vos postes, votre serveur ou le cloud",
                "Un support après livraison et des évolutions au rythme de vos besoins",
            ],
        },
        "automation": {
            "name": "Automatisation",
            "short": "Automatiser le reporting, le traitement des données et les tâches répétitives avec Python et JavaScript — pour que votre équipe se concentre sur l’essentiel.",
            "intro": [
                "Chaque entreprise a des tâches faites à la main, encore et encore : télécharger des fichiers, mettre à jour des tableurs, recopier des données d’une application à l’autre, produire le même rapport chaque semaine. J’automatise ces processus de bout en bout avec Python et JavaScript.",
                "Le résultat s’exécute selon un planning ou d’un simple clic, avec des journaux clairs et des alertes — et une validation humaine partout où c’est nécessaire.",
            ],
            "why": [
                "Le travail manuel et répétitif est lent, coûteux et source d’erreurs. Une formule erronée ou un fichier oublié peut fausser discrètement un rapport sur lequel tout le monde s’appuie. L’automatisation rend ces processus plus rapides, cohérents et vérifiables.",
                "Elle libère aussi vos collaborateurs qualifiés des tâches à faible valeur. Quelques heures gagnées chaque semaine représentent vite des journées de capacité en plus chaque mois.",
            ],
            "expect": [
                "Une revue de vos processus pour identifier où l’automatisation rapporte le plus",
                "Rapports automatisés, gestion de fichiers et transferts de données entre applications",
                "Automatisation de tableurs et d’Excel/VBA, automatisation web et navigateur",
                "Exécution planifiée ou à la demande, avec journalisation et alertes d’erreur",
                "Une documentation pour que votre équipe comprenne et maîtrise chaque étape",
                "Des résultats mesurés : temps gagné et erreurs évitées",
            ],
        },
        "technical-consulting": {
            "name": "Conseil technique",
            "short": "Une expertise technique indépendante sur vos systèmes, votre architecture et vos mises en œuvre — forte de plus de 25 ans en marchés de capitaux, risques et IT.",
            "intro": [
                "Choisir, déployer ou moderniser un système implique des décisions difficiles à défaire. J’apporte un conseil technique indépendant et opérationnel pour vous aider à les prendre en confiance : évaluation des options, conception de la solution et accompagnement de la mise en œuvre.",
                "Avec plus de 25 ans en marchés de capitaux, risques et IT — notamment à des postes seniors chez Finastra, Murex, Calypso et Reuters — j’ai travaillé sur des plateformes de trading, de risque et de back-office pour de grandes banques en Europe et au Moyen-Orient.",
            ],
            "why": [
                "Les choix technologiques pèsent pendant des années sur les coûts, les risques et l’agilité. Un regard extérieur expérimenté vous aide à challenger les propositions des éditeurs, à éviter la sur-ingénierie et à concentrer le budget sur l’essentiel.",
                "Ayant travaillé à la fois côté éditeur et côté client, je sais où les projets dérapent habituellement — et comment l’éviter.",
            ],
            "expect": [
                "Un diagnostic de vos systèmes, de votre architecture et de vos flux de données",
                "Conception de solution et recommandations technologiques",
                "Évaluation d’éditeurs et de progiciels, notamment de plateformes de trading et de risque",
                "Planification de la mise en œuvre, stratégie de migration et revue des risques",
                "Un appui opérationnel sur l’intégration, les données et le SQL",
                "Un reporting clair et régulier auprès de la direction",
            ],
        },
        "business-analysis": {
            "name": "Analyse métier",
            "short": "Faire le lien entre les besoins métier et la mise en œuvre technique : exigences claires, spécifications et analyse des processus.",
            "intro": [
                "Un projet échoue rarement à cause de la seule technologie. Il échoue quand les besoins métier et la mise en œuvre technique s’éloignent l’un de l’autre. En tant que business analyst, je me place entre les deux : je comprends ce dont vos équipes ont besoin, je le traduis en exigences précises et je m’assure que ce qui est construit y correspond vraiment.",
                "J’écoute, je spécifie, je livre : des ateliers structurés, une documentation claire et un suivi rapproché, de la première réunion à la mise en production.",
            ],
            "why": [
                "Des exigences floues sont le bug le plus coûteux d’un projet. Chaque malentendu découvert tardivement coûte du temps, du budget et de la confiance.",
                "Une analyse structurée en amont — menée par quelqu’un qui parle à la fois le langage du métier et celui de la technique — permet de tenir le périmètre, les délais et le budget.",
            ],
            "expect": [
                "Des ateliers avec les parties prenantes pour recueillir besoins et contraintes",
                "Spécifications fonctionnelles, user stories et critères d’acceptation",
                "Cartographie des processus et analyse d’écarts entre l’existant et la cible",
                "Analyses de données et requêtes SQL pour éclairer les décisions",
                "Stratégie de test, coordination de la recette (UAT) et accompagnement à la mise en production",
                "Une documentation qui reste utile après la fin du projet",
            ],
        },
        "ai-integration": {
            "name": "Intégration de l’IA",
            "short": "Mettre l’IA au service de la création de contenu, du traitement de documents et du reporting — avec les bons garde-fous.",
            "intro": [
                "L’intelligence artificielle est aujourd’hui un outil concret pour les petites équipes, pas seulement pour les grands groupes. Je vous aide à la mettre au service de tâches précises : rédaction et mise en forme de contenus, synthèse de documents et extraction d’informations, tri des demandes entrantes et production de rapports récurrents.",
                "J’intègre les services d’IA aux outils que vous utilisez déjà, en Python et JavaScript, pour que les résultats arrivent là où vous en avez besoin — avec une validation humaine quand c’est nécessaire.",
            ],
            "why": [
                "Bien utilisée, l’IA peut transformer des heures de lecture, de rédaction et de mise en forme en quelques minutes.",
                "Utilisée sans précaution, elle produit des erreurs et crée des risques pour vos données et votre réputation. La valeur vient d’un flux bien cadré, avec des règles claires, des étapes de contrôle et une supervision humaine — c’est exactement ainsi que je les conçois.",
            ],
            "expect": [
                "L’identification des cas d’usage où l’IA apporte un vrai retour",
                "Des chaînes de création de contenu et de traitement de documents assistées par l’IA",
                "L’intégration à vos outils : e-mail, tableurs, CMS et API",
                "Des garde-fous : étapes de relecture, contrôles et protection des données",
                "Documentation et séance de prise en main pour que votre équipe garde la main",
                "Des résultats mesurés : temps gagné et qualité améliorée",
            ],
        },
    },
}
