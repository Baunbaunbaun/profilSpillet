# profiles.py

# Du behøver ikke tænke på fil-endelser (.jpg/.png) her. 
# Scriptet finder selv billedet, så længe navnet (f.eks. "Rasmus") passer.

PROFILES = [
    {
        "name": "ALAN TURING",
        "title": "THE CODEBREAKER",
        "image_base_name": "Alan",
        "theme_color": "#00b4d8", # Elektrisk Blå (The Digital Age)
        "stats": [
            ("LOGIK & MATEMATIK", 100), # Uovervindelig her
            ("INNOVATION", 99),
            ("KRYPTERING", 98),
            ("STAMINA (LØB)", 94), # Han var næsten OL-niveau maratonløber!
            ("SOCIAL KONFORMITET", 5)
        ],
        "ability_title": "UNIVERSAL MACHINE",
        "ability_desc": "Kan beregne det umulige og knække enhver kode."
    },
    {
        "name": "KAREN BLIXEN",
        "title": "THE STORYTELLER",
        "image_base_name": "Karen",
        "theme_color": "#6f1d1b", # Dyb mørkerød (Afrikansk jord / Passion)
        "stats": [
            ("FORTÆLLEKUNST", 100), # Uovervindelig. Hun ER historien.
            ("RESILIENS", 96),      # Overlevede syfilis, konkurs og hjertesorg.
            ("EVENTYRLYST", 94),    # Safari, løvejagt og flyvning i 1920'erne.
            ("KARISMA", 92),
            ("ØKONOMISK SANS", 15)  # Farmen gik jo desværre konkurs...
        ],
        "ability_title": "SCHEHERAZADE",
        "ability_desc": "Kan forvandle enhver tragedie til en udødelig historie."
    },
    {
        "name": "BRUCE LEE",
        "title": "THE PIONEER",
        "image_base_name": "Bruce",
        "theme_color": "#f9c74f", # Den ikoniske gule farve (Game of Death)
        "stats": [
            ("ADAPTABILITY (BE WATER)", 100),
            ("INNOVATION", 99),
            ("DISCIPLIN", 98),
            ("FILOSOFI", 95),
            ("KONFORMITET", 1)
        ],
        "ability_title": "ONE INCH PUNCH",
        "ability_desc": "Maksimal effekt med minimal afstand. Slår hårdere end han ser ud."
    },
]