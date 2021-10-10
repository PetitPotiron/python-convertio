from typing import Optional


def lang_code(language: str) -> str:
    lang_codes = {
        'afrikaans': 'afr',
        'albanian': 'sqi',
        'arabic': 'ara',
        'armenian-eastern': 'arm_east',
        'armenian-western': 'arm_west',
        'azeri-cyrillic': 'aze_cyrl',
        'azeri-latin': 'aze',
        'basque': 'eus',
        'belarusian': 'bel',
        'bulgarian': 'bul',
        'catalan': 'cat',
        'cebuano': 'ceb',
        'chinese-simplified': 'chi_sim',
        'chinese-traditional': 'chi_tra',
        'croatian': 'hrv',
        'czech': 'ces',
        'danish': 'dan',
        'dutch': 'dut',
        'dutch-belgian': 'nld',
        'english': 'eng',
        'esperanto': 'epo',
        'estonian': 'est',
        'fijian': 'fij',
        'finnish': 'fin',
        'french': 'fra',
        'galician': 'glg',
        'german': 'deu',
        'greek': 'grk',
        'hawaiian': 'haw',
        'hebrew': 'heb',
        'hungarian': 'hun',
        'icelandic': 'isl',
        'indonesian': 'ind',
        'irish': 'gle',
        'italian': 'ita',
        'japanese': 'jpn',
        'kazakh': 'kaz',
        'kirghiz': 'kir',
        'kongo': 'jon',
        'korean': 'kor',
        'kurdish': 'kur',
        'latin': 'lat',
        'latvian': 'lav',
        'lithuanian': 'lit',
        'macedonian': 'mkd',
        'malay-malaysian': 'mal',
        'maltese': 'mlt',
        'norwegian-bokmal': 'nor',
        'polish': 'pol',
        'portuguese': ' por',
        'portuguese-brazilian': 'bra',
        'romanian': ' ron',
        'russian': 'rus',
        'scottish': 'sco',
        'serbian-cyrillic': 'srp',
        'serbian-latin': 'srp_latn',
        'slovak': 'slk',
        'slovenian': 'slv',
        'somali': 'som',
        'spanish': 'spa',
        'swahili': 'swa',
        'swedish': 'swe',
        'tagalog': 'tgl',
        'tahitian': 'tah',
        'tajik': 'tgk',
        'tatar': 'tat',
        'thai': 'tha',
        'turkish': 'tur',
        'turkmen': 'turk',
        'uighur-cyrillic': 'uig_cyr',
        'uighur-latin': 'uig',
        'ukrainian': 'ukr',
        'uzbek-cyrillic': 'uzb_cyrl',
        'uzbek-latin': 'uzb',
        'vietnamese': 'vie',
        'welsh': 'cym'
    }
    if not language.lower() in lang_codes.values():
        return lang_codes[language.lower()]
    else:
        return language


class Lang:
    def __init__(self, language: str):
        self.code = lang_code(language)


class Options:
    def __init__(self, langs: list[Lang], page_nums: Optional[str] = None) -> None:
        self.langs: list[str] = []
        for lang in langs:
            self.langs.append(lang.code)
        self.page_nums = page_nums
