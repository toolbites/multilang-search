"""
Google ki saari languages (133) — har ek ka mulk (gl), Google domain aur free-engine region.
code = Google Translate code (Google search 'hl' bhi yahi, sirf chand mein farq)
"""

# code: (Naam, gl country, ddg region)
_L = {
    "af": ("Afrikaans", "za", "za-en"), "sq": ("Albanian", "al", "wt-wt"), "am": ("Amharic", "et", "wt-wt"),
    "ar": ("Arabic", "sa", "xa-ar"), "hy": ("Armenian", "am", "wt-wt"), "as": ("Assamese", "in", "in-en"),
    "ay": ("Aymara", "bo", "wt-wt"), "az": ("Azerbaijani", "az", "wt-wt"), "bm": ("Bambara", "ml", "wt-wt"),
    "eu": ("Basque", "es", "es-es"), "be": ("Belarusian", "by", "wt-wt"), "bn": ("Bengali", "bd", "wt-wt"),
    "bho": ("Bhojpuri", "in", "in-en"), "bs": ("Bosnian", "ba", "wt-wt"), "bg": ("Bulgarian", "bg", "bg-bg"),
    "ca": ("Catalan", "es", "ct-ca"), "ceb": ("Cebuano", "ph", "ph-tl"), "ny": ("Chichewa", "mw", "wt-wt"),
    "zh-CN": ("Chinese (Simplified)", "cn", "cn-zh"), "zh-TW": ("Chinese (Traditional)", "tw", "tw-tzh"),
    "co": ("Corsican", "fr", "fr-fr"), "hr": ("Croatian", "hr", "hr-hr"), "cs": ("Czech", "cz", "cz-cs"),
    "da": ("Danish", "dk", "dk-da"), "dv": ("Dhivehi", "mv", "wt-wt"), "doi": ("Dogri", "in", "in-en"),
    "nl": ("Dutch", "nl", "nl-nl"), "en": ("English", "us", "us-en"), "eo": ("Esperanto", "us", "wt-wt"),
    "et": ("Estonian", "ee", "ee-et"), "ee": ("Ewe", "gh", "wt-wt"), "tl": ("Filipino", "ph", "ph-tl"),
    "fi": ("Finnish", "fi", "fi-fi"), "fr": ("French", "fr", "fr-fr"), "fy": ("Frisian", "nl", "nl-nl"),
    "gl": ("Galician", "es", "es-es"), "ka": ("Georgian", "ge", "wt-wt"), "de": ("German", "de", "de-de"),
    "el": ("Greek", "gr", "gr-el"), "gn": ("Guarani", "py", "wt-wt"), "gu": ("Gujarati", "in", "in-en"),
    "ht": ("Haitian Creole", "ht", "wt-wt"), "ha": ("Hausa", "ng", "wt-wt"), "haw": ("Hawaiian", "us", "us-en"),
    "iw": ("Hebrew", "il", "il-he"), "hi": ("Hindi", "in", "in-en"), "hmn": ("Hmong", "la", "wt-wt"),
    "hu": ("Hungarian", "hu", "hu-hu"), "is": ("Icelandic", "is", "wt-wt"), "ig": ("Igbo", "ng", "wt-wt"),
    "ilo": ("Ilocano", "ph", "ph-tl"), "id": ("Indonesian", "id", "id-id"), "ga": ("Irish", "ie", "ie-en"),
    "it": ("Italian", "it", "it-it"), "ja": ("Japanese", "jp", "jp-jp"), "jw": ("Javanese", "id", "id-id"),
    "kn": ("Kannada", "in", "in-en"), "kk": ("Kazakh", "kz", "wt-wt"), "km": ("Khmer", "kh", "wt-wt"),
    "rw": ("Kinyarwanda", "rw", "wt-wt"), "gom": ("Konkani", "in", "in-en"), "ko": ("Korean", "kr", "kr-kr"),
    "kri": ("Krio", "sl", "wt-wt"), "ku": ("Kurdish (Kurmanji)", "tr", "tr-tr"), "ckb": ("Kurdish (Sorani)", "iq", "xa-ar"),
    "ky": ("Kyrgyz", "kg", "wt-wt"), "lo": ("Lao", "la", "wt-wt"), "la": ("Latin", "va", "wt-wt"),
    "lv": ("Latvian", "lv", "lv-lv"), "ln": ("Lingala", "cd", "wt-wt"), "lt": ("Lithuanian", "lt", "lt-lt"),
    "lg": ("Luganda", "ug", "wt-wt"), "lb": ("Luxembourgish", "lu", "wt-wt"), "mk": ("Macedonian", "mk", "wt-wt"),
    "mai": ("Maithili", "in", "in-en"), "mg": ("Malagasy", "mg", "wt-wt"), "ms": ("Malay", "my", "my-ms"),
    "ml": ("Malayalam", "in", "in-en"), "mt": ("Maltese", "mt", "wt-wt"), "mi": ("Maori", "nz", "nz-en"),
    "mr": ("Marathi", "in", "in-en"), "mni-Mtei": ("Meiteilon (Manipuri)", "in", "in-en"), "lus": ("Mizo", "in", "in-en"),
    "mn": ("Mongolian", "mn", "wt-wt"), "my": ("Myanmar (Burmese)", "mm", "wt-wt"), "ne": ("Nepali", "np", "wt-wt"),
    "no": ("Norwegian", "no", "no-no"), "or": ("Odia (Oriya)", "in", "in-en"), "om": ("Oromo", "et", "wt-wt"),
    "ps": ("Pashto", "af", "wt-wt"), "fa": ("Persian", "ir", "wt-wt"), "pl": ("Polish", "pl", "pl-pl"),
    "pt": ("Portuguese", "br", "br-pt"), "pa": ("Punjabi", "in", "in-en"), "qu": ("Quechua", "pe", "pe-es"),
    "ro": ("Romanian", "ro", "ro-ro"), "ru": ("Russian", "ru", "ru-ru"), "sm": ("Samoan", "ws", "wt-wt"),
    "sa": ("Sanskrit", "in", "in-en"), "gd": ("Scots Gaelic", "gb", "uk-en"), "nso": ("Sepedi", "za", "za-en"),
    "sr": ("Serbian", "rs", "wt-wt"), "st": ("Sesotho", "ls", "wt-wt"), "sn": ("Shona", "zw", "wt-wt"),
    "sd": ("Sindhi", "pk", "pk-en"), "si": ("Sinhala", "lk", "wt-wt"), "sk": ("Slovak", "sk", "sk-sk"),
    "sl": ("Slovenian", "si", "sl-sl"), "so": ("Somali", "so", "wt-wt"), "es": ("Spanish", "es", "es-es"),
    "su": ("Sundanese", "id", "id-id"), "sw": ("Swahili", "ke", "wt-wt"), "sv": ("Swedish", "se", "se-sv"),
    "tg": ("Tajik", "tj", "wt-wt"), "ta": ("Tamil", "in", "in-en"), "tt": ("Tatar", "ru", "ru-ru"),
    "te": ("Telugu", "in", "in-en"), "th": ("Thai", "th", "th-th"), "ti": ("Tigrinya", "er", "wt-wt"),
    "ts": ("Tsonga", "za", "za-en"), "tr": ("Turkish", "tr", "tr-tr"), "tk": ("Turkmen", "tm", "wt-wt"),
    "ak": ("Twi", "gh", "wt-wt"), "uk": ("Ukrainian", "ua", "ua-uk"), "ur": ("Urdu", "pk", "pk-en"),
    "ug": ("Uyghur", "cn", "wt-wt"), "uz": ("Uzbek", "uz", "wt-wt"), "vi": ("Vietnamese", "vn", "vn-vi"),
    "cy": ("Welsh", "gb", "uk-en"), "xh": ("Xhosa", "za", "za-en"), "yi": ("Yiddish", "il", "il-he"),
    "yo": ("Yoruba", "ng", "wt-wt"), "zu": ("Zulu", "za", "za-en"),
}

# Mulk -> Google domain
_DOMAIN = {
    "us": "google.com", "za": "google.co.za", "al": "google.al", "et": "google.com.et", "sa": "google.com.sa",
    "am": "google.am", "bo": "google.com.bo", "az": "google.az", "ml": "google.ml", "es": "google.es",
    "by": "google.by", "bd": "google.com.bd", "in": "google.co.in", "ba": "google.ba", "bg": "google.bg",
    "ph": "google.com.ph", "mw": "google.mw", "cn": "google.com.hk", "tw": "google.com.tw", "fr": "google.fr",
    "hr": "google.hr", "cz": "google.cz", "dk": "google.dk", "mv": "google.mv", "nl": "google.nl",
    "ee": "google.ee", "gh": "google.com.gh", "fi": "google.fi", "ge": "google.ge", "de": "google.de",
    "gr": "google.gr", "py": "google.com.py", "ht": "google.ht", "ng": "google.com.ng", "il": "google.co.il",
    "la": "google.la", "hu": "google.hu", "is": "google.is", "id": "google.co.id", "ie": "google.ie",
    "it": "google.it", "jp": "google.co.jp", "kz": "google.kz", "kh": "google.com.kh", "rw": "google.rw",
    "kr": "google.co.kr", "sl": "google.com.sl", "tr": "google.com.tr", "iq": "google.iq", "kg": "google.kg",
    "va": "google.com", "lv": "google.lv", "cd": "google.cd", "lt": "google.lt", "ug": "google.co.ug",
    "lu": "google.lu", "mk": "google.mk", "mg": "google.mg", "my": "google.com.my", "mt": "google.com.mt",
    "nz": "google.co.nz", "mn": "google.mn", "mm": "google.com.mm", "np": "google.com.np", "no": "google.no",
    "af": "google.com.af", "ir": "google.com", "pl": "google.pl", "br": "google.com.br", "pe": "google.com.pe",
    "ro": "google.ro", "ru": "google.ru", "ws": "google.ws", "gb": "google.co.uk", "rs": "google.rs",
    "ls": "google.co.ls", "zw": "google.co.zw", "pk": "google.com.pk", "lk": "google.lk", "sk": "google.sk",
    "si": "google.si", "so": "google.so", "ke": "google.co.ke", "se": "google.se", "tj": "google.com.tj",
    "th": "google.co.th", "er": "google.com", "tm": "google.tm", "ua": "google.com.ua", "uz": "google.co.uz",
    "vn": "google.com.vn",
}

# Google search 'hl' jahan Translate code se alag hai
_HL = {"jw": "jv", "mni-Mtei": "mni", "gom": "kok", "ckb": "ckb", "zh-CN": "zh-CN", "zh-TW": "zh-TW"}

# Purane short codes bhi chalein (website/purani settings)
ALIASES = {"he": "iw"}

LANGUAGES = {
    code: {
        "name": name,
        "translate": code,
        "hl": _HL.get(code, code),
        "gl": gl,
        "google_domain": _DOMAIN.get(gl, "google.com"),
        "region": region,
    }
    for code, (name, gl, region) in _L.items()
}


def resolve(codes):
    """['all'] ya codes ki list -> sahi codes. Ghalat codes alag wapas."""
    if not codes or codes == ["all"] or "all" in codes:
        return list(LANGUAGES), []
    ok, bad = [], []
    for c in codes:
        c = ALIASES.get(c, c)
        (ok if c in LANGUAGES else bad).append(c)
    return list(dict.fromkeys(ok)), bad
