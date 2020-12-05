class TestCases:
    def test_cases_getWilayaByCode(self):
        cases = [
            {
                'input': 1,
                'expected': {
                    "mattricule":
                    1,
                    "name":
                    "Adrar",
                    "name_ar":
                    "أدرار",
                    "name_en":
                    "Adrar",
                    "phoneCodes": [49],
                    "postalCodes": [
                        1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008,
                        1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017,
                        1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026,
                        1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035,
                        1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044,
                        1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053,
                        1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062,
                        1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071,
                        1072, 1073, 1074
                    ],
                    "dairats": [{
                        "code":
                        101,
                        "name":
                        "ADRAR",
                        "name_ar":
                        "أدرار",
                        "name_en":
                        "ADRAR",
                        "baladyiats": [{
                            "code": 101,
                            "name": "ADRAR",
                            "name_en": "ADRAR",
                            "name_ar": "أدرار"
                        }, {
                            "code": 121,
                            "name": "OULED AHMED TIMMI",
                            "name_en": "OULED AHMED TIMMI",
                            "name_ar": "أولاد أحمد تيمي"
                        }, {
                            "code": 122,
                            "name": "BOUDA",
                            "name_en": "BOUDA",
                            "name_ar": "بودة"
                        }]
                    }, {
                        "code":
                        103,
                        "name":
                        "CHAROUINE",
                        "name_ar":
                        "شروين",
                        "name_en":
                        "CHAROUINE",
                        "baladyiats": [{
                            "code": 103,
                            "name": "CHAROUINE",
                            "name_en": "CHAROUINE",
                            "name_ar": "شروين"
                        }, {
                            "code": 124,
                            "name": "TALMINE",
                            "name_en": "TALMINE",
                            "name_ar": "طالمين"
                        }, {
                            "code": 127,
                            "name": "OULED AISSA",
                            "name_en": "OULED AISSA",
                            "name_ar": "أولاد عيسى"
                        }]
                    }, {
                        "code":
                        104,
                        "name":
                        "REGGANE",
                        "name_ar":
                        "رقان",
                        "name_en":
                        "REGGANE",
                        "baladyiats": [{
                            "code": 104,
                            "name": "REGGANE",
                            "name_en": "REGGANE",
                            "name_ar": "رقان"
                        }, {
                            "code": 118,
                            "name": "SALI",
                            "name_en": "SALI",
                            "name_ar": "سالي"
                        }]
                    }, {
                        "code":
                        108,
                        "name":
                        "TSABIT",
                        "name_ar":
                        "تسابيت",
                        "name_en":
                        "TSABIT",
                        "baladyiats": [{
                            "code": 108,
                            "name": "TSABIT",
                            "name_en": "TSABIT",
                            "name_ar": "تسابيت"
                        }, {
                            "code": 126,
                            "name": "SEBAA",
                            "name_en": "SEBAA",
                            "name_ar": "السبع"
                        }]
                    }, {
                        "code":
                        109,
                        "name":
                        "TIMIMOUN",
                        "name_ar":
                        "تيميمون",
                        "name_en":
                        "TIMIMOUN",
                        "baladyiats": [{
                            "code": 109,
                            "name": "TIMIMOUN",
                            "name_en": "TIMIMOUN",
                            "name_ar": "تيميمون"
                        }, {
                            "code": 110,
                            "name": "OULED SAID",
                            "name_en": "OULED SAID",
                            "name_ar": "أولاد السعيد"
                        }]
                    }, {
                        "code":
                        111,
                        "name":
                        "ZAOUIAT KOUNTA",
                        "name_ar":
                        "زاوية كنتة",
                        "name_en":
                        "ZAOUIAT KOUNTA",
                        "baladyiats": [{
                            "code": 105,
                            "name": "IN ZGHMIR",
                            "name_en": "IN ZGHMIR",
                            "name_ar": "إن زغمير"
                        }, {
                            "code": 111,
                            "name": "ZAOUIET KOUNTA",
                            "name_en": "ZAOUIET KOUNTA",
                            "name_ar": "زاوية كنتة"
                        }]
                    }, {
                        "code":
                        112,
                        "name":
                        "AOULEF",
                        "name_ar":
                        "أولف",
                        "name_en":
                        "AOULEF",
                        "baladyiats": [{
                            "code": 106,
                            "name": "TIT",
                            "name_en": "TIT",
                            "name_ar": "تيت"
                        }, {
                            "code": 112,
                            "name": "AOULEF",
                            "name_en": "AOULEF",
                            "name_ar": "أولف"
                        }, {
                            "code": 113,
                            "name": "TIMEKTEN",
                            "name_en": "TIMEKTEN",
                            "name_ar": "تيمقتن"
                        }, {
                            "code": 119,
                            "name": "AKABLI",
                            "name_en": "AKABLI",
                            "name_ar": "اقبلي"
                        }]
                    }, {
                        "code":
                        115,
                        "name":
                        "FENOUGHIL",
                        "name_ar":
                        "فنوغيل",
                        "name_en":
                        "FENOUGHIL",
                        "baladyiats": [{
                            "code": 102,
                            "name": "TAMEST",
                            "name_en": "TAMEST",
                            "name_ar": "تامست"
                        }, {
                            "code": 114,
                            "name": "TAMANTIT",
                            "name_en": "TAMANTIT",
                            "name_ar": "تامنطيط"
                        }, {
                            "code": 115,
                            "name": "FENOUGHIL",
                            "name_en": "FENOUGHIL",
                            "name_ar": "فنوغيل"
                        }]
                    }, {
                        "code":
                        116,
                        "name":
                        "TINERKOUK",
                        "name_ar":
                        "تنركوك",
                        "name_en":
                        "TINERKOUK",
                        "baladyiats": [{
                            "code": 107,
                            "name": "KSAR KADDOUR",
                            "name_en": "KSAR KADDOUR",
                            "name_ar": "قصر قدور"
                        }, {
                            "code": 116,
                            "name": "TINERKOUK",
                            "name_en": "TINERKOUK",
                            "name_ar": "تنركوك"
                        }]
                    }, {
                        "code":
                        123,
                        "name":
                        "AOUGROUT",
                        "name_ar":
                        "أوقروت",
                        "name_en":
                        "AOUGROUT",
                        "baladyiats": [{
                            "code": 117,
                            "name": "DELDOUL",
                            "name_en": "DELDOUL",
                            "name_ar": "دلدول"
                        }, {
                            "code": 120,
                            "name": "METARFA",
                            "name_en": "METARFA",
                            "name_ar": "المطارفة"
                        }, {
                            "code": 123,
                            "name": "AOUGROUT",
                            "name_en": "AOUGROUT",
                            "name_ar": "أوقروت"
                        }]
                    }, {
                        "code":
                        125,
                        "name":
                        "BORDJ BADJI MOKHTAR",
                        "name_ar":
                        "برج باجي مختار",
                        "name_en":
                        "BORDJ BADJI MOKHTAR",
                        "baladyiats": [{
                            "code": 125,
                            "name": "BORDJ BADJI MOKHTAR",
                            "name_en": "BORDJ BADJI MOKHTAR",
                            "name_ar": "برج باجي مختار"
                        }, {
                            "code": 128,
                            "name": "TIMIAOUINE",
                            "name_en": "TIMIAOUINE",
                            "name_ar": "تيمياوين"
                        }]
                    }, {
                        "code": 1090,
                        "name": "TIMIMOUN (wilaya déléguée)",
                        "name_ar": "تيميمون (ولاية منتدبة)",
                        "name_en": "TIMIMOUN (wilaya déléguée)"
                    }, {
                        "code":
                        1250,
                        "name":
                        "BORDJ BADJI MOKHTAR (wilaya déléguée)",
                        "name_ar":
                        "برج باجي مختار (ولاية منتدبة)",
                        "name_en":
                        "BORDJ BADJI MOKHTAR (wilaya déléguée)"
                    }],
                    "adjacentWilayas": [37, 8, 32, 3, 47, 11]
                }
            },
            {
                'input': 2,
                'expected': {
                    "mattricule":
                    2,
                    "name":
                    "Chlef",
                    "name_ar":
                    "الشلف",
                    "name_en":
                    "Chlef",
                    "phoneCodes": [27],
                    "postalCodes": [
                        2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                        2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,
                        2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026,
                        2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035,
                        2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044,
                        2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053,
                        2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062,
                        2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071,
                        2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080,
                        2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089,
                        2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098,
                        2099, 2100
                    ],
                    "dairats": [{
                        "code":
                        201,
                        "name":
                        "CHLEF",
                        "name_ar":
                        "الشلف",
                        "name_en":
                        "CHLEF",
                        "baladyiats": [{
                            "code": 201,
                            "name": "CHLEF",
                            "name_en": "CHLEF",
                            "name_ar": "الشلف"
                        }, {
                            "code": 219,
                            "name": "SENDJAS",
                            "name_en": "SENDJAS",
                            "name_ar": "سنجاس"
                        }, {
                            "code": 233,
                            "name": "OUM DROU",
                            "name_en": "OUM DROU",
                            "name_ar": "أم الدروع"
                        }]
                    }, {
                        "code":
                        202,
                        "name":
                        "TENES",
                        "name_ar":
                        "تنس",
                        "name_en":
                        "TENES",
                        "baladyiats": [{
                            "code": 202,
                            "name": "TENES",
                            "name_en": "TENES",
                            "name_ar": "تنس"
                        }, {
                            "code": 211,
                            "name": "SIDI AKKACHA",
                            "name_en": "SIDI AKKACHA",
                            "name_ar": "سيدي عكاشة"
                        }, {
                            "code": 225,
                            "name": "SIDI ABDERRAHMANE",
                            "name_en": "SIDI ABDERRAHMANE",
                            "name_ar": "سيدي عبد الرحمن"
                        }]
                    }, {
                        "code":
                        204,
                        "name":
                        "EL KARIMIA",
                        "name_ar":
                        "الكريمية",
                        "name_en":
                        "EL KARIMIA",
                        "baladyiats": [{
                            "code": 204,
                            "name": "EL KARIMIA",
                            "name_en": "EL KARIMIA",
                            "name_ar": "الكريمية"
                        }, {
                            "code": 209,
                            "name": "HARCHOUN",
                            "name_en": "HARCHOUN",
                            "name_ar": "حرشون"
                        }, {
                            "code": 235,
                            "name": "BENI  BOUATTAB",
                            "name_en": "BENI  BOUATTAB",
                            "name_ar": "بني بوعتاب"
                        }]
                    }, {
                        "code":
                        206,
                        "name":
                        "TAOUGRIT",
                        "name_ar":
                        "تاوقريت",
                        "name_en":
                        "TAOUGRIT",
                        "baladyiats": [{
                            "code": 206,
                            "name": "TAOUGRIT",
                            "name_en": "TAOUGRIT",
                            "name_ar": "تاوقريت"
                        }, {
                            "code": 217,
                            "name": "DAHRA",
                            "name_en": "DAHRA",
                            "name_ar": "الظهرة"
                        }]
                    }, {
                        "code":
                        207,
                        "name":
                        "BENI HAOUA",
                        "name_ar":
                        "بني حواء",
                        "name_en":
                        "BENI HAOUA",
                        "baladyiats": [{
                            "code": 207,
                            "name": "BENI HAOUA",
                            "name_en": "BENI HAOUA",
                            "name_ar": "بني حواء"
                        }, {
                            "code": 216,
                            "name": "OUED GOUSSINE",
                            "name_en": "OUED GOUSSINE",
                            "name_ar": "وادي قوسين"
                        }, {
                            "code": 234,
                            "name": "BREIRA",
                            "name_en": "BREIRA",
                            "name_ar": "بريرة"
                        }]
                    }, {
                        "code":
                        210,
                        "name":
                        "OULED FARES",
                        "name_ar":
                        "أولاد فارس",
                        "name_en":
                        "OULED FARES",
                        "baladyiats": [{
                            "code": 210,
                            "name": "OULED FARES",
                            "name_en": "OULED FARES",
                            "name_ar": "أولاد فارس"
                        }, {
                            "code": 224,
                            "name": "CHETTIA",
                            "name_en": "CHETTIA",
                            "name_ar": "الشطية"
                        }, {
                            "code": 228,
                            "name": "LABIOD MEDJADJA",
                            "name_en": "LABIOD MEDJADJA",
                            "name_ar": "الأبيض مجاجة"
                        }]
                    }, {
                        "code":
                        212,
                        "name":
                        "BOUKADIR",
                        "name_ar":
                        "بوقادير",
                        "name_en":
                        "BOUKADIR",
                        "baladyiats": [{
                            "code": 208,
                            "name": "SOBHA",
                            "name_en": "SOBHA",
                            "name_ar": "الصبحة"
                        }, {
                            "code": 212,
                            "name": "BOUKADIR",
                            "name_en": "BOUKADIR",
                            "name_ar": "بوقادير"
                        }, {
                            "code": 221,
                            "name": "OUED SLY",
                            "name_en": "OUED SLY",
                            "name_ar": "وادي سلي"
                        }]
                    }, {
                        "code":
                        220,
                        "name":
                        "ZEBOUDJA",
                        "name_ar":
                        "الزبوجة",
                        "name_en":
                        "ZEBOUDJA",
                        "baladyiats": [{
                            "code": 203,
                            "name": "BENAIRIA",
                            "name_en": "BENAIRIA",
                            "name_ar": "بنايرية"
                        }, {
                            "code": 220,
                            "name": "ZEBOUDJA",
                            "name_en": "ZEBOUDJA",
                            "name_ar": "الزبوجة"
                        }, {
                            "code": 231,
                            "name": "BOUZEGHAIA",
                            "name_en": "BOUZEGHAIA",
                            "name_ar": "بوزغاية"
                        }]
                    }, {
                        "code":
                        222,
                        "name":
                        "ABOU EL HASSANE",
                        "name_ar":
                        "أبو الحسن",
                        "name_en":
                        "ABOU EL HASSANE",
                        "baladyiats": [{
                            "code": 205,
                            "name": "TADJENA",
                            "name_en": "TADJENA",
                            "name_ar": "تاجنة"
                        }, {
                            "code": 214,
                            "name": "TALASSA",
                            "name_en": "TALASSA",
                            "name_ar": "تلعصة"
                        }, {
                            "code": 222,
                            "name": "ABOU EL HASSANE",
                            "name_en": "ABOU EL HASSANE",
                            "name_ar": "أبو الحسن"
                        }]
                    }, {
                        "code":
                        223,
                        "name":
                        "EL MARSA",
                        "name_ar":
                        "المرسى",
                        "name_en":
                        "EL MARSA",
                        "baladyiats": [{
                            "code": 223,
                            "name": "EL MARSA",
                            "name_en": "EL MARSA",
                            "name_ar": "المرسى"
                        }, {
                            "code": 226,
                            "name": "MOUSSADEK",
                            "name_en": "MOUSSADEK",
                            "name_ar": "مصدق"
                        }]
                    }, {
                        "code":
                        229,
                        "name":
                        "OUED FODDA",
                        "name_ar":
                        "وادي الفضة",
                        "name_en":
                        "OUED FODDA",
                        "baladyiats": [{
                            "code": 213,
                            "name": "BENI RACHED",
                            "name_en": "BENI RACHED",
                            "name_ar": "بني راشد"
                        }, {
                            "code": 218,
                            "name": "OULED ABBES",
                            "name_en": "OULED ABBES",
                            "name_ar": "أولاد عباس"
                        }, {
                            "code": 229,
                            "name": "OUED FODDA",
                            "name_en": "OUED FODDA",
                            "name_ar": "وادي الفضة"
                        }]
                    }, {
                        "code":
                        230,
                        "name":
                        "OULED BEN ABDELKADER",
                        "name_ar":
                        "أولاد بن عبد القادر",
                        "name_en":
                        "OULED BEN ABDELKADER",
                        "baladyiats": [{
                            "code": 227,
                            "name": "EL HADJADJ",
                            "name_en": "EL HADJADJ",
                            "name_ar": "الحجاج"
                        }, {
                            "code": 230,
                            "name": "OULED BEN ABDELKADER",
                            "name_en": "OULED BEN ABDELKADER",
                            "name_ar": "أولاد بن عبد القادر"
                        }]
                    }, {
                        "code":
                        232,
                        "name":
                        "AIN MERANE",
                        "name_ar":
                        "عين مران",
                        "name_en":
                        "AIN MERANE",
                        "baladyiats": [{
                            "code": 215,
                            "name": "HERENFA",
                            "name_en": "HERENFA",
                            "name_ar": "الهرانفة"
                        }, {
                            "code": 232,
                            "name": "AIN MERANE",
                            "name_en": "AIN MERANE",
                            "name_ar": "عين مران"
                        }]
                    }],
                    "adjacentWilayas": [27, 48, 7, 38, 44, 42]
                }
            },
            {
                'input': 3,
                'expected': {
                    "mattricule":
                    3,
                    "name":
                    "Laghouat",
                    "name_ar":
                    "الأغواط",
                    "name_en":
                    "Laghouat",
                    "phoneCodes": [29],
                    "postalCodes": [
                        3000, 3001, 3002, 3003, 3004, 3005, 3006, 3007, 3008,
                        3009, 3010, 3011, 3012, 3013, 3014, 3015, 3016, 3017,
                        3018, 3019, 3020, 3021, 3022, 3023, 3024, 3025, 3026,
                        3027, 3028, 3030, 3031, 3032, 3033, 3034, 3035, 3036,
                        3037, 3038, 3040, 3041, 3042, 3043, 3044, 3046, 3047,
                        3048, 3049, 3050, 3051, 3052, 3053, 3054
                    ],
                    "dairats": [{
                        "code":
                        301,
                        "name":
                        "LAGHOUAT",
                        "name_ar":
                        "الأغواط",
                        "name_en":
                        "LAGHOUAT",
                        "baladyiats": [{
                            "code": 301,
                            "name": "LAGHOUAT",
                            "name_en": "LAGHOUAT",
                            "name_ar": "الأغواط"
                        }]
                    }, {
                        "code":
                        302,
                        "name":
                        "KSAR EL HIRANE",
                        "name_ar":
                        "قصر الحيران",
                        "name_en":
                        "KSAR EL HIRANE",
                        "baladyiats": [{
                            "code": 302,
                            "name": "KSAR EL HIRANE",
                            "name_en": "KSAR EL HIRANE",
                            "name_ar": "قصر الحيران"
                        }, {
                            "code": 303,
                            "name": "BENACER BENCHOHRA",
                            "name_en": "BENACER BENCHOHRA",
                            "name_ar": "بن ناصر بن شهرة"
                        }]
                    }, {
                        "code":
                        304,
                        "name":
                        "SIDI MAKHLOUF",
                        "name_ar":
                        "سيدي مخلوف",
                        "name_en":
                        "SIDI MAKHLOUF",
                        "baladyiats": [{
                            "code": 304,
                            "name": "SIDI MAKHLOUF",
                            "name_en": "SIDI MAKHLOUF",
                            "name_ar": "سيدي مخلوف"
                        }, {
                            "code": 320,
                            "name": "EL ASSAFIA",
                            "name_en": "EL ASSAFIA",
                            "name_ar": "العسافية"
                        }]
                    }, {
                        "code":
                        306,
                        "name":
                        "HASSI R'MEL",
                        "name_ar":
                        "حاسي الرمل",
                        "name_en":
                        "HASSI R'MEL",
                        "baladyiats": [{
                            "code": 305,
                            "name": "HASSI DELAA",
                            "name_en": "HASSI DELAA",
                            "name_ar": "حاسي الدلاعة"
                        }, {
                            "code": 306,
                            "name": "HASSI R'MEL",
                            "name_en": "HASSI R'MEL",
                            "name_ar": "حاسي الرمل"
                        }]
                    }, {
                        "code":
                        307,
                        "name":
                        "AIN MADHI",
                        "name_ar":
                        "عين ماضي",
                        "name_en":
                        "AIN MADHI",
                        "baladyiats": [{
                            "code": 307,
                            "name": "AIN MADHI",
                            "name_en": "AIN MADHI",
                            "name_ar": "عين ماضي"
                        }, {
                            "code": 308,
                            "name": "TADJEMOUT",
                            "name_en": "TADJEMOUT",
                            "name_ar": "تاجموت"
                        }, {
                            "code": 309,
                            "name": "KHENEG",
                            "name_en": "KHENEG",
                            "name_ar": "الخنق"
                        }, {
                            "code": 318,
                            "name": "TADJROUNA",
                            "name_en": "TADJROUNA",
                            "name_ar": "تاجرونة"
                        }, {
                            "code": 323,
                            "name": "EL HAOUAITA",
                            "name_en": "EL HAOUAITA",
                            "name_ar": "الحويطة"
                        }]
                    }, {
                        "code":
                        310,
                        "name":
                        "GUELTAT SIDI SAAD",
                        "name_ar":
                        "قتلة سيدي سعيد",
                        "name_en":
                        "GUELTAT SIDI SAAD",
                        "baladyiats": [{
                            "code": 310,
                            "name": "GUELTAT SIDI SAAD",
                            "name_en": "GUELTAT SIDI SAAD",
                            "name_ar": "قلتة سيدي سعد"
                        }, {
                            "code": 311,
                            "name": "AIN SIDI ALI",
                            "name_en": "AIN SIDI ALI",
                            "name_ar": "عين سيدي علي"
                        }, {
                            "code": 312,
                            "name": "EL BEIDHA",
                            "name_en": "EL BEIDHA",
                            "name_ar": "البيضاء"
                        }]
                    }, {
                        "code":
                        313,
                        "name":
                        "BRIDA",
                        "name_ar":
                        "بريدة",
                        "name_en":
                        "BRIDA",
                        "baladyiats": [{
                            "code": 313,
                            "name": "BRIDA",
                            "name_en": "BRIDA",
                            "name_ar": "بريدة"
                        }, {
                            "code": 315,
                            "name": "HADJ MECHRI",
                            "name_en": "HADJ MECHRI",
                            "name_ar": "الحاج مشري"
                        }, {
                            "code": 317,
                            "name": "TAOUIALA",
                            "name_en": "TAOUIALA",
                            "name_ar": "تاويالة"
                        }]
                    }, {
                        "code":
                        314,
                        "name":
                        "EL GHICHA",
                        "name_ar":
                        "الغيشة",
                        "name_en":
                        "EL GHICHA",
                        "baladyiats": [{
                            "code": 314,
                            "name": "EL GHICHA",
                            "name_en": "EL GHICHA",
                            "name_ar": "الغيشة"
                        }]
                    }, {
                        "code":
                        319,
                        "name":
                        "AFLOU",
                        "name_ar":
                        "أفلو",
                        "name_en":
                        "AFLOU",
                        "baladyiats": [{
                            "code": 316,
                            "name": "SEBGAG",
                            "name_en": "SEBGAG",
                            "name_ar": "سبقاق"
                        }, {
                            "code": 319,
                            "name": "AFLOU",
                            "name_en": "AFLOU",
                            "name_ar": "أفلو"
                        }, {
                            "code": 324,
                            "name": "SIDI BOUZID",
                            "name_en": "SIDI BOUZID",
                            "name_ar": "سيدي بوزيد"
                        }]
                    }, {
                        "code":
                        321,
                        "name":
                        "OUED MORRA",
                        "name_ar":
                        "وادي مرة",
                        "name_en":
                        "OUED MORRA",
                        "baladyiats": [{
                            "code": 321,
                            "name": "OUED MORRA",
                            "name_en": "OUED MORRA",
                            "name_ar": "وادي مرة"
                        }, {
                            "code": 322,
                            "name": "OUED M'ZI",
                            "name_en": "OUED M'ZI",
                            "name_ar": "وادي مزي"
                        }]
                    }],
                    "adjacentWilayas": [32, 47, 17, 14]
                }
            },
            {
                'input': 6,
                'expected': {
                    "mattricule":
                    6,
                    "name":
                    "Béjaïa",
                    "name_ar":
                    "بجاية",
                    "name_en":
                    "Béjaïa",
                    "phoneCodes": [34],
                    "postalCodes": [
                        6000, 6001, 6002, 6003, 6004, 6005, 6006, 6007, 6008,
                        6009, 6010, 6011, 6012, 6013, 6014, 6015, 6016, 6017,
                        6018, 6019, 6020, 6021, 6022, 6023, 6024, 6025, 6026,
                        6027, 6028, 6029, 6030, 6031, 6032, 6033, 6034, 6035,
                        6036, 6037, 6038, 6039, 6040, 6041, 6042, 6043, 6044,
                        6045, 6046, 6047, 6048, 6049, 6050, 6051, 6052, 6053,
                        6054, 6055, 6056, 6057, 6058, 6059, 6060, 6061, 6062,
                        6063, 6064, 6065, 6066, 6067, 6068, 6069, 6070, 6071,
                        6072, 6073, 6074, 6075, 6076, 6077, 6078, 6079, 6080,
                        6081, 6082, 6083, 6084, 6085, 6086, 6087, 6088, 6089,
                        6090, 6091, 6092, 6093, 6094, 6095, 6096, 6097, 6098,
                        6099, 6100, 6101, 6102, 6103, 6104, 6106, 6107, 6108,
                        6109, 6110, 6111, 6112, 6113, 6114, 6115, 6116, 6117,
                        6118, 6119, 6120, 6121, 6122, 6123, 6124, 6125, 6126,
                        6127, 6128, 6129, 6130, 6131, 6132, 6133, 6134, 6135,
                        6136, 6137, 6138, 6139, 6140, 6141, 6142, 6143, 6144
                    ],
                    "dairats": [{
                        "code":
                        601,
                        "name":
                        "BEJAIA",
                        "name_ar":
                        "بجاية",
                        "name_en":
                        "BEJAIA",
                        "baladyiats": [{
                            "code": 601,
                            "name": "BEJAIA",
                            "name_en": "BEJAIA",
                            "name_ar": "بجاية"
                        }, {
                            "code": 651,
                            "name": "OUED GHIR",
                            "name_en": "OUED GHIR",
                            "name_ar": "وادي غير"
                        }]
                    }, {
                        "code":
                        602,
                        "name":
                        "AMIZOUR",
                        "name_ar":
                        "أميزور",
                        "name_en":
                        "AMIZOUR",
                        "baladyiats": [{
                            "code": 602,
                            "name": "AMIZOUR",
                            "name_en": "AMIZOUR",
                            "name_ar": "أميزور"
                        }, {
                            "code": 603,
                            "name": "FERAOUN",
                            "name_en": "FERAOUN",
                            "name_ar": "فرعون"
                        }, {
                            "code": 612,
                            "name": "SMAOUN",
                            "name_en": "SMAOUN",
                            "name_ar": "سمعون"
                        }, {
                            "code": 623,
                            "name": "BENI DJELLIL",
                            "name_en": "BENI DJELLIL",
                            "name_ar": "بني جليل"
                        }]
                    }, {
                        "code":
                        607,
                        "name":
                        "TIMEZRIT",
                        "name_ar":
                        "تيمزريت",
                        "name_en":
                        "TIMEZRIT",
                        "baladyiats": [{
                            "code": 607,
                            "name": "TIMEZRIT",
                            "name_en": "TIMEZRIT",
                            "name_ar": "تيمزريت"
                        }]
                    }, {
                        "code":
                        608,
                        "name":
                        "SOUK EL TENINE",
                        "name_ar":
                        "سوق الإثنين",
                        "name_en":
                        "SOUK EL TENINE",
                        "baladyiats": [{
                            "code": 608,
                            "name": "SOUK EL TENINE",
                            "name_en": "SOUK EL TENINE",
                            "name_ar": "سوق لإثنين"
                        }, {
                            "code": 641,
                            "name": "MELBOU",
                            "name_en": "MELBOU",
                            "name_ar": "مالبو"
                        }, {
                            "code": 646,
                            "name": "TAMRIDJET",
                            "name_en": "TAMRIDJET",
                            "name_ar": "تامريجت"
                        }]
                    }, {
                        "code":
                        611,
                        "name":
                        "TICHY",
                        "name_ar":
                        "تيشي",
                        "name_en":
                        "TICHY",
                        "baladyiats": [{
                            "code": 611,
                            "name": "TICHY",
                            "name_en": "TICHY",
                            "name_ar": "تيشي"
                        }, {
                            "code": 633,
                            "name": "TALA HAMZA",
                            "name_en": "TALA HAMZA",
                            "name_ar": "تالة حمزة"
                        }, {
                            "code": 648,
                            "name": "BOUKHELIFA",
                            "name_en": "BOUKHELIFA",
                            "name_ar": "بوخليفة"
                        }]
                    }, {
                        "code":
                        617,
                        "name":
                        "IGHIL ALI",
                        "name_ar":
                        "إغيل علي",
                        "name_en":
                        "IGHIL ALI",
                        "baladyiats": [{
                            "code": 617,
                            "name": "IGHIL-ALI",
                            "name_en": "IGHIL-ALI",
                            "name_ar": "إغيل علي"
                        }, {
                            "code": 628,
                            "name": "AIT R'ZINE",
                            "name_en": "AIT R'ZINE",
                            "name_ar": "أيت رزين"
                        }]
                    }, {
                        "code":
                        620,
                        "name":
                        "DARGUINA",
                        "name_ar":
                        "درقينة",
                        "name_en":
                        "DARGUINA",
                        "baladyiats": [{
                            "code": 620,
                            "name": "DARGUINA",
                            "name_en": "DARGUINA",
                            "name_ar": "درقينة"
                        }, {
                            "code": 631,
                            "name": "TASKRIOUT",
                            "name_en": "TASKRIOUT",
                            "name_ar": "تاسكريوت"
                        }, {
                            "code": 647,
                            "name": "AIT-SMAIL",
                            "name_en": "AIT-SMAIL",
                            "name_ar": "أيت إسماعيل"
                        }]
                    }, {
                        "code":
                        622,
                        "name":
                        "AOKAS",
                        "name_ar":
                        "أوقاس",
                        "name_en":
                        "AOKAS",
                        "baladyiats": [{
                            "code": 622,
                            "name": "AOKAS",
                            "name_en": "AOKAS",
                            "name_ar": "أوقاس"
                        }, {
                            "code": 649,
                            "name": "TIZI-N'BERBER",
                            "name_en": "TIZI-N'BERBER",
                            "name_ar": "تيزي نبربر"
                        }]
                    }, {
                        "code":
                        624,
                        "name":
                        "ADEKAR",
                        "name_ar":
                        "أدكار",
                        "name_en":
                        "ADEKAR",
                        "baladyiats": [{
                            "code": 604,
                            "name": "TAOURIT IGHIL",
                            "name_en": "TAOURIT IGHIL",
                            "name_ar": "تاوريرت إغيل"
                        }, {
                            "code": 624,
                            "name": "ADEKAR",
                            "name_en": "ADEKAR",
                            "name_ar": "أدكار"
                        }, {
                            "code": 635,
                            "name": "BENI K'SILA",
                            "name_en": "BENI K'SILA",
                            "name_ar": "بني كسيلة"
                        }]
                    }, {
                        "code":
                        625,
                        "name":
                        "AKBOU",
                        "name_ar":
                        "أقبو",
                        "name_en":
                        "AKBOU",
                        "baladyiats": [{
                            "code": 605,
                            "name": "CHELLATA",
                            "name_en": "CHELLATA",
                            "name_ar": "شلاطة"
                        }, {
                            "code": 606,
                            "name": "TAMOKRA",
                            "name_en": "TAMOKRA",
                            "name_ar": "تامقرة"
                        }, {
                            "code": 615,
                            "name": "IGHRAM",
                            "name_en": "IGHRAM",
                            "name_ar": "اغرم"
                        }, {
                            "code": 625,
                            "name": "AKBOU",
                            "name_en": "AKBOU",
                            "name_ar": "أقبو"
                        }]
                    }, {
                        "code":
                        626,
                        "name":
                        "SEDDOUK",
                        "name_ar":
                        "صدوق",
                        "name_en":
                        "SEDDOUK",
                        "baladyiats": [{
                            "code": 609,
                            "name": "M'CISNA",
                            "name_en": "M'CISNA",
                            "name_ar": "مسيسنة"
                        }, {
                            "code": 616,
                            "name": "AMALOU",
                            "name_en": "AMALOU",
                            "name_ar": "أمالو"
                        }, {
                            "code": 626,
                            "name": "SEDDOUK",
                            "name_en": "SEDDOUK",
                            "name_ar": "صدوق"
                        }, {
                            "code": 637,
                            "name": "BOUHAMZA",
                            "name_en": "BOUHAMZA",
                            "name_ar": "بوحمزة"
                        }]
                    }, {
                        "code":
                        627,
                        "name":
                        "TAZMALT",
                        "name_ar":
                        "تازملت",
                        "name_en":
                        "TAZMALT",
                        "baladyiats": [{
                            "code": 627,
                            "name": "TAZMALT",
                            "name_en": "TAZMALT",
                            "name_ar": "تازمالت"
                        }, {
                            "code": 638,
                            "name": "BENI-MALLIKECHE",
                            "name_en": "BENI-MALLIKECHE",
                            "name_ar": "بني مليكش"
                        }, {
                            "code": 652,
                            "name": "BOUDJELLIL",
                            "name_en": "BOUDJELLIL",
                            "name_ar": "بو جليل"
                        }]
                    }, {
                        "code":
                        629,
                        "name":
                        "CHEMINI",
                        "name_ar":
                        "شميني",
                        "name_en":
                        "CHEMINI",
                        "baladyiats": [{
                            "code": 629,
                            "name": "CHEMINI",
                            "name_en": "CHEMINI",
                            "name_ar": "شميني"
                        }, {
                            "code": 630,
                            "name": "SOUK OUFELLA",
                            "name_en": "SOUK OUFELLA",
                            "name_ar": "سوق اوفلا"
                        }, {
                            "code": 632,
                            "name": "TIBANE",
                            "name_en": "TIBANE",
                            "name_ar": "طيبان"
                        }, {
                            "code": 642,
                            "name": "AKFADOU",
                            "name_en": "AKFADOU",
                            "name_ar": "أكفادو"
                        }]
                    }, {
                        "code":
                        634,
                        "name":
                        "BARBACHA",
                        "name_ar":
                        "برباشة",
                        "name_en":
                        "BARBACHA",
                        "baladyiats": [{
                            "code": 613,
                            "name": "KENDIRA",
                            "name_en": "KENDIRA",
                            "name_ar": "كنديرة"
                        }, {
                            "code": 634,
                            "name": "BARBACHA",
                            "name_en": "BARBACHA",
                            "name_ar": "برباشة"
                        }]
                    }, {
                        "code":
                        636,
                        "name":
                        "IFRI OUZELLAGUENE",
                        "name_ar":
                        "إفري أوزلاقن",
                        "name_en":
                        "IFRI OUZELLAGUENE",
                        "baladyiats": [{
                            "code": 636,
                            "name": "OUZELLAGUEN",
                            "name_en": "OUZELLAGUEN",
                            "name_ar": "أوزلاقن"
                        }]
                    }, {
                        "code":
                        639,
                        "name":
                        "SIDI AICH",
                        "name_ar":
                        "سيدي عيش",
                        "name_en":
                        "SIDI AICH",
                        "baladyiats": [{
                            "code": 610,
                            "name": "TINEBDAR",
                            "name_en": "TINEBDAR",
                            "name_ar": "تينبدار"
                        }, {
                            "code": 614,
                            "name": "TIFRA",
                            "name_en": "TIFRA",
                            "name_ar": "تيفرة"
                        }, {
                            "code": 621,
                            "name": "SIDI AYAD",
                            "name_en": "SIDI AYAD",
                            "name_ar": "سيدي عياد"
                        }, {
                            "code": 639,
                            "name": "SIDI-AICH",
                            "name_en": "SIDI-AICH",
                            "name_ar": "سيدي عيش"
                        }, {
                            "code": 643,
                            "name": "LEFLAYE",
                            "name_en": "LEFLAYE",
                            "name_ar": "الفلاي"
                        }]
                    }, {
                        "code":
                        640,
                        "name":
                        "EL KSEUR",
                        "name_ar":
                        "القصر",
                        "name_en":
                        "EL KSEUR",
                        "baladyiats": [{
                            "code": 618,
                            "name": "FENAIA IL MATEN",
                            "name_en": "FENAIA IL MATEN",
                            "name_ar": "فناية الماثن"
                        }, {
                            "code": 619,
                            "name": "TOUDJA",
                            "name_en": "TOUDJA",
                            "name_ar": "توجة"
                        }, {
                            "code": 640,
                            "name": "EL KSEUR",
                            "name_en": "EL KSEUR",
                            "name_ar": "القصر"
                        }]
                    }, {
                        "code":
                        644,
                        "name":
                        "KHERRATA",
                        "name_ar":
                        "خراطة",
                        "name_en":
                        "KHERRATA",
                        "baladyiats": [{
                            "code": 644,
                            "name": "KHERRATA",
                            "name_en": "KHERRATA",
                            "name_ar": "خراطة"
                        }, {
                            "code": 645,
                            "name": "DRA EL CAID",
                            "name_en": "DRA EL CAID",
                            "name_ar": "ذراع القايد"
                        }]
                    }, {
                        "code":
                        650,
                        "name":
                        "BENI MAOUCHE",
                        "name_ar":
                        "بني معوش",
                        "name_en":
                        "BENI MAOUCHE",
                        "baladyiats": [{
                            "code": 650,
                            "name": "BENIMAOUCHE",
                            "name_en": "BENIMAOUCHE",
                            "name_ar": "بني معوش"
                        }]
                    }],
                    "adjacentWilayas": [15, 10, 34, 19, 18]
                }
            },
        ]
        return cases

    def test_cases_getWilayaByZipCode(self):
        cases = [{
            'input': 7001,
            'expected': {
                "mattricule":
                7,
                "name":
                "Biskra",
                "name_ar":
                "بسكرة",
                "name_en":
                "Biskra",
                "phoneCodes": [33],
                "postalCodes": [
                    7000, 7001, 7002, 7003, 7004, 7005, 7006, 7007, 7008, 7009,
                    7010, 7011, 7012, 7013, 7014, 7015, 7016, 7017, 7018, 7019,
                    7020, 7021, 7022, 7023, 7024, 7025, 7026, 7027, 7028, 7029,
                    7030, 7031, 7032, 7033, 7034, 7035, 7036, 7037, 7038, 7039,
                    7040, 7041, 7042, 7043, 7044, 7045, 7046, 7047, 7048, 7049,
                    7050, 7051, 7052, 7053, 7054, 7055, 7056, 7057, 7058, 7059,
                    7060, 7061, 7062, 7063, 7064, 7065, 7066, 7067, 7068, 7069,
                    7070, 7071, 7072, 7073, 7074, 7075, 7076, 7077, 7078, 7079,
                    7080, 7081, 7082, 7083, 7084, 7085, 7086, 7087, 7088, 7089,
                    7090, 7091, 7092, 7093, 7094, 7095
                ],
                "dairats": [{
                    "code":
                    701,
                    "name":
                    "BISKRA",
                    "name_ar":
                    "بسكرة",
                    "name_en":
                    "BISKRA",
                    "baladyiats": [{
                        "code": 701,
                        "name": "BISKRA",
                        "name_en": "BISKRA",
                        "name_ar": "بسكرة"
                    }, {
                        "code": 732,
                        "name": "EL HADJAB",
                        "name_en": "EL HADJAB",
                        "name_ar": "الحاجب"
                    }]
                }, {
                    "code":
                    705,
                    "name":
                    "OULED DJELLAL",
                    "name_ar":
                    "أولاد جلال",
                    "name_en":
                    "OULED DJELLAL",
                    "baladyiats": [{
                        "code": 705,
                        "name": "OULED DJELLAL",
                        "name_en": "OULED DJELLAL",
                        "name_ar": "أولاد جلال"
                    }, {
                        "code": 709,
                        "name": "DOUCEN",
                        "name_en": "DOUCEN",
                        "name_ar": "الدوسن"
                    }, {
                        "code": 710,
                        "name": "CHAIBA",
                        "name_en": "CHAIBA",
                        "name_ar": "الشعيبة"
                    }]
                }, {
                    "code":
                    708,
                    "name":
                    "SIDI KHALED",
                    "name_ar":
                    "سيدي  خالد",
                    "name_en":
                    "SIDI KHALED",
                    "baladyiats": [{
                        "code": 706,
                        "name": "RAS EL MIAD",
                        "name_en": "RAS EL MIAD",
                        "name_ar": "رأس الميعاد"
                    }, {
                        "code": 707,
                        "name": "BESBES",
                        "name_en": "BESBES",
                        "name_ar": "بسباس"
                    }, {
                        "code": 708,
                        "name": "SIDI KHALED",
                        "name_en": "SIDI KHALED",
                        "name_ar": "سيدي  خالد"
                    }]
                }, {
                    "code":
                    711,
                    "name":
                    "SIDI OKBA",
                    "name_ar":
                    "سيدي عقبة",
                    "name_en":
                    "SIDI OKBA",
                    "baladyiats": [{
                        "code": 704,
                        "name": "CHETMA",
                        "name_en": "CHETMA",
                        "name_ar": "شتمة"
                    }, {
                        "code": 711,
                        "name": "SIDI OKBA",
                        "name_en": "SIDI OKBA",
                        "name_ar": "سيدي عقبة"
                    }, {
                        "code": 713,
                        "name": "EL HAOUCH",
                        "name_en": "EL HAOUCH",
                        "name_ar": "الحوش"
                    }, {
                        "code": 714,
                        "name": "AIN NAGA",
                        "name_en": "AIN NAGA",
                        "name_ar": "عين الناقة"
                    }]
                }, {
                    "code":
                    712,
                    "name":
                    "MECHOUNECHE",
                    "name_ar":
                    "مشونش",
                    "name_en":
                    "MECHOUNECHE",
                    "baladyiats": [{
                        "code": 712,
                        "name": "M'CHOUNECHE",
                        "name_en": "M'CHOUNECHE",
                        "name_ar": "مشونش"
                    }]
                }, {
                    "code":
                    715,
                    "name":
                    "ZERIBET EL OUED",
                    "name_ar":
                    "زريبة الوادي",
                    "name_en":
                    "ZERIBET EL OUED",
                    "baladyiats": [{
                        "code": 715,
                        "name": "ZERIBET EL OUED",
                        "name_en": "ZERIBET EL OUED",
                        "name_ar": "زريبة الوادي"
                    }, {
                        "code": 716,
                        "name": "EL FEIDH",
                        "name_en": "EL FEIDH",
                        "name_ar": "الفيض"
                    }, {
                        "code": 728,
                        "name": "MEZIRAA",
                        "name_en": "MEZIRAA",
                        "name_ar": "المزيرعة"
                    }, {
                        "code": 733,
                        "name": "KHENGUET SIDI NADJI",
                        "name_en": "KHENGUET SIDI NADJI",
                        "name_ar": "خنقة سيدي ناجي"
                    }]
                }, {
                    "code":
                    717,
                    "name":
                    "EL KANTARA",
                    "name_ar":
                    "القنطرة",
                    "name_en":
                    "EL KANTARA",
                    "baladyiats": [{
                        "code": 717,
                        "name": "EL KANTARA",
                        "name_en": "EL KANTARA",
                        "name_ar": "القنطرة"
                    }, {
                        "code": 718,
                        "name": "AIN ZAATOUT",
                        "name_en": "AIN ZAATOUT",
                        "name_ar": "عين زعطوط"
                    }]
                }, {
                    "code":
                    719,
                    "name":
                    "EL OUTAYA",
                    "name_ar":
                    "الوطاية",
                    "name_en":
                    "EL OUTAYA",
                    "baladyiats": [{
                        "code": 719,
                        "name": "EL OUTAYA",
                        "name_en": "EL OUTAYA",
                        "name_ar": "الوطاية"
                    }]
                }, {
                    "code":
                    720,
                    "name":
                    "DJEMORAH",
                    "name_ar":
                    "جمورة",
                    "name_en":
                    "DJEMORAH",
                    "baladyiats": [{
                        "code": 703,
                        "name": "BRANIS",
                        "name_en": "BRANIS",
                        "name_ar": "برانيس"
                    }, {
                        "code": 720,
                        "name": "DJEMORAH",
                        "name_en": "DJEMORAH",
                        "name_ar": "جمورة"
                    }]
                }, {
                    "code":
                    721,
                    "name":
                    "TOLGA",
                    "name_ar":
                    "طولقة",
                    "name_en":
                    "TOLGA",
                    "baladyiats": [{
                        "code": 721,
                        "name": "TOLGA",
                        "name_en": "TOLGA",
                        "name_ar": "طولقة"
                    }, {
                        "code": 723,
                        "name": "LICHANA",
                        "name_en": "LICHANA",
                        "name_ar": "ليشانة"
                    }, {
                        "code": 727,
                        "name": "BORDJ BEN AZZOUZ",
                        "name_en": "BORDJ BEN AZZOUZ",
                        "name_ar": "برج بن عزوز"
                    }, {
                        "code": 729,
                        "name": "BOUCHAKROUN",
                        "name_en": "BOUCHAKROUN",
                        "name_ar": "بوشقرون"
                    }]
                }, {
                    "code":
                    724,
                    "name":
                    "OURLAL",
                    "name_ar":
                    "أورلال",
                    "name_en":
                    "OURLAL",
                    "baladyiats": [{
                        "code": 702,
                        "name": "OUMACHE",
                        "name_en": "OUMACHE",
                        "name_ar": "أوماش"
                    }, {
                        "code": 722,
                        "name": "LIOUA",
                        "name_en": "LIOUA",
                        "name_ar": "ليوة"
                    }, {
                        "code": 724,
                        "name": "OURLAL",
                        "name_en": "OURLAL",
                        "name_ar": "أورلال"
                    }, {
                        "code": 725,
                        "name": "M'LILI",
                        "name_en": "M'LILI",
                        "name_ar": "مليلي"
                    }, {
                        "code": 730,
                        "name": "MEKHADMA",
                        "name_en": "MEKHADMA",
                        "name_ar": "مخادمة"
                    }]
                }, {
                    "code":
                    726,
                    "name":
                    "FOUGHALA",
                    "name_ar":
                    "فوغالة",
                    "name_en":
                    "FOUGHALA",
                    "baladyiats": [{
                        "code": 726,
                        "name": "FOUGHALA",
                        "name_en": "FOUGHALA",
                        "name_ar": "فوغالة"
                    }, {
                        "code": 731,
                        "name": "EL GHROUS",
                        "name_en": "EL GHROUS",
                        "name_ar": "الغروس"
                    }]
                }, {
                    "code": 7050,
                    "name": "OULED DJELLAL (wilaya déléguée)",
                    "name_ar": "أولاد جلال (ولاية منتدبة)",
                    "name_en": "OULED DJELLAL (wilaya déléguée)"
                }],
                "adjacentWilayas": [17, 28, 5, 40, 39, 30]
            }
        }, {
            'input': 14010,
            'expected': {
                "mattricule":
                14,
                "name":
                "Tiaret",
                "name_ar":
                "تيارت",
                "name_en":
                "Tiaret",
                "phoneCodes": [46],
                "postalCodes": [
                    14000, 14001, 14002, 14003, 14004, 14005, 14006, 14007,
                    14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015,
                    14016, 14017, 14018, 14019, 14020, 14021, 14023, 14024,
                    14025, 14026, 14027, 14028, 14029, 14030, 14031, 14032,
                    14033, 14034, 14035, 14036, 14037, 14038, 14039, 14040,
                    14041, 14042, 14043, 14044, 14045, 14046, 14047, 14048,
                    14049, 14050, 14051, 14052, 14053, 14054, 14055, 14056,
                    14057, 14058, 14059, 14060, 14061, 14062, 14063, 14064,
                    14065, 14066, 14067, 14068, 14069, 14070, 14071, 14072,
                    14073, 14074, 14075, 14076, 14077, 14078, 14079, 14080,
                    14081
                ],
                "dairats": [{
                    "code":
                    1401,
                    "name":
                    "TIARET",
                    "name_ar":
                    "تيارت",
                    "name_en":
                    "TIARET",
                    "baladyiats": [{
                        "code": 1401,
                        "name": "TIARET",
                        "name_en": "TIARET",
                        "name_ar": "تيارت"
                    }]
                }, {
                    "code":
                    1402,
                    "name":
                    "MEDROUSSA",
                    "name_ar":
                    "مدروسة",
                    "name_en":
                    "MEDROUSSA",
                    "baladyiats": [{
                        "code": 1402,
                        "name": "MEDROUSSA",
                        "name_en": "MEDROUSSA",
                        "name_ar": "مدروسة"
                    }, {
                        "code": 1407,
                        "name": "SIDI BAKHTI",
                        "name_en": "SIDI BAKHTI",
                        "name_ar": "سيدي بختي"
                    }, {
                        "code": 1412,
                        "name": "MELLAKOU",
                        "name_en": "MELLAKOU",
                        "name_ar": "ملاكو"
                    }]
                }, {
                    "code":
                    1406,
                    "name":
                    "AIN DEHEB",
                    "name_ar":
                    "عين الذهب",
                    "name_en":
                    "AIN DEHEB",
                    "baladyiats": [{
                        "code": 1406,
                        "name": "AIN DEHEB",
                        "name_en": "AIN DEHEB",
                        "name_ar": "عين الذهب"
                    }, {
                        "code": 1420,
                        "name": "NAIMA",
                        "name_en": "NAIMA",
                        "name_ar": "النعيمة"
                    }, {
                        "code": 1436,
                        "name": "CHEHAIMA",
                        "name_en": "CHEHAIMA",
                        "name_ar": "شحيمة"
                    }]
                }, {
                    "code":
                    1413,
                    "name":
                    "DAHMOUNI",
                    "name_ar":
                    "دحموني",
                    "name_en":
                    "DAHMOUNI",
                    "baladyiats": [{
                        "code": 1403,
                        "name": "AIN BOUCHEKIF",
                        "name_en": "AIN BOUCHEKIF",
                        "name_ar": "عين بوشقيف"
                    }, {
                        "code": 1413,
                        "name": "DAHMOUNI",
                        "name_en": "DAHMOUNI",
                        "name_ar": "دحموني"
                    }]
                }, {
                    "code":
                    1414,
                    "name":
                    "RAHOUIA",
                    "name_ar":
                    "رحوية",
                    "name_en":
                    "RAHOUIA",
                    "baladyiats": [{
                        "code": 1414,
                        "name": "RAHOUIA",
                        "name_en": "RAHOUIA",
                        "name_ar": "الرحوية"
                    }, {
                        "code": 1422,
                        "name": "GUERTOUFA",
                        "name_en": "GUERTOUFA",
                        "name_ar": "قرطوفة"
                    }]
                }, {
                    "code":
                    1415,
                    "name":
                    "MAHDIA",
                    "name_ar":
                    "مهدية",
                    "name_en":
                    "MAHDIA",
                    "baladyiats": [{
                        "code": 1405,
                        "name": "AIN DZARIT",
                        "name_en": "AIN DZARIT",
                        "name_ar": "عين دزاريت"
                    }, {
                        "code": 1415,
                        "name": "MAHDIA",
                        "name_en": "MAHDIA",
                        "name_ar": "مهدية"
                    }, {
                        "code": 1425,
                        "name": "SEBAINE",
                        "name_en": "SEBAINE",
                        "name_ar": "السبعين"
                    }, {
                        "code": 1431,
                        "name": "NADORAH",
                        "name_en": "NADORAH",
                        "name_ar": "الناظورة"
                    }]
                }, {
                    "code":
                    1416,
                    "name":
                    "SOUGUEUR",
                    "name_ar":
                    "السوقر",
                    "name_en":
                    "SOUGUEUR",
                    "baladyiats": [{
                        "code": 1416,
                        "name": "SOUGUEUR",
                        "name_en": "SOUGUEUR",
                        "name_ar": "السوقر"
                    }, {
                        "code": 1417,
                        "name": "SI ABDELGHANI",
                        "name_en": "SI ABDELGHANI",
                        "name_ar": "سي عبد الغني"
                    }, {
                        "code": 1426,
                        "name": "TOUSNINA",
                        "name_en": "TOUSNINA",
                        "name_ar": "توسنينة"
                    }, {
                        "code": 1441,
                        "name": "FAIDJA",
                        "name_en": "FAIDJA",
                        "name_ar": "الفايجة"
                    }]
                }, {
                    "code":
                    1421,
                    "name":
                    "MEGHILA",
                    "name_ar":
                    "مغيلة",
                    "name_en":
                    "MEGHILA",
                    "baladyiats": [{
                        "code": 1411,
                        "name": "SEBT",
                        "name_en": "SEBT",
                        "name_ar": "السبت"
                    }, {
                        "code": 1421,
                        "name": "MEGHILA",
                        "name_en": "MEGHILA",
                        "name_ar": "مغيلة"
                    }, {
                        "code": 1423,
                        "name": "SIDI HOSNI",
                        "name_en": "SIDI HOSNI",
                        "name_ar": "سيدي حسني"
                    }]
                }, {
                    "code":
                    1427,
                    "name":
                    "FRENDA",
                    "name_ar":
                    "فرندة",
                    "name_en":
                    "FRENDA",
                    "baladyiats": [{
                        "code": 1418,
                        "name": "AIN EL HADID",
                        "name_en": "AIN EL HADID",
                        "name_ar": "عين الحديد"
                    }, {
                        "code": 1427,
                        "name": "FRENDA",
                        "name_en": "FRENDA",
                        "name_ar": "فرندة"
                    }, {
                        "code": 1437,
                        "name": "TAKHEMARET",
                        "name_en": "TAKHEMARET",
                        "name_ar": "تخمرت"
                    }]
                }, {
                    "code":
                    1428,
                    "name":
                    "AIN KERMES",
                    "name_ar":
                    "عين كرمس",
                    "name_en":
                    "AIN KERMES",
                    "baladyiats": [{
                        "code": 1408,
                        "name": "MEDRISSA",
                        "name_en": "MEDRISSA",
                        "name_ar": "مدريسة"
                    }, {
                        "code": 1410,
                        "name": "MADNA",
                        "name_en": "MADNA",
                        "name_ar": "مادنة"
                    }, {
                        "code": 1419,
                        "name": "DJEBILET ROSFA",
                        "name_en": "DJEBILET ROSFA",
                        "name_ar": "جبيلات الرصفاء"
                    }, {
                        "code": 1428,
                        "name": "AIN KERMES",
                        "name_en": "AIN KERMES",
                        "name_ar": "عين كرمس"
                    }, {
                        "code": 1438,
                        "name": "SIDI ABDERRAHMANE",
                        "name_en": "SIDI ABDERRAHMANE",
                        "name_ar": "سيدي عبد الرحمن"
                    }]
                }, {
                    "code":
                    1429,
                    "name":
                    "KSAR CHELLALA",
                    "name_ar":
                    "قصر الشلالة",
                    "name_en":
                    "KSAR CHELLALA",
                    "baladyiats": [{
                        "code": 1409,
                        "name": "ZMALET EL EMIR ABDELKADE",
                        "name_en": "ZMALET EL EMIR ABDELKADE",
                        "name_ar": "زمالة  الأمير عبد القادر"
                    }, {
                        "code": 1429,
                        "name": "KSAR CHELLALA",
                        "name_en": "KSAR CHELLALA",
                        "name_ar": "قصر الشلالة"
                    }, {
                        "code": 1439,
                        "name": "SERGHINE",
                        "name_en": "SERGHINE",
                        "name_ar": "سرغين"
                    }]
                }, {
                    "code":
                    1433,
                    "name":
                    "OUED LILI",
                    "name_ar":
                    "وادي ليلي",
                    "name_en":
                    "OUED LILI",
                    "baladyiats": [{
                        "code": 1404,
                        "name": "SIDI ALI MELLAL",
                        "name_en": "SIDI ALI MELLAL",
                        "name_ar": "سيدي علي ملال"
                    }, {
                        "code": 1433,
                        "name": "OUED LILLI",
                        "name_en": "OUED LILLI",
                        "name_ar": "وادي ليلي"
                    }, {
                        "code": 1442,
                        "name": "TIDDA",
                        "name_en": "TIDDA",
                        "name_ar": "تيدة"
                    }]
                }, {
                    "code":
                    1434,
                    "name":
                    "MECHRAA SFA",
                    "name_ar":
                    "مشرع الصفا",
                    "name_en":
                    "MECHRAA SFA",
                    "baladyiats": [{
                        "code": 1424,
                        "name": "DJILLALI BEN AMAR",
                        "name_en": "DJILLALI BEN AMAR",
                        "name_ar": "جيلالي بن عمار"
                    }, {
                        "code": 1432,
                        "name": "TAGDEMPT",
                        "name_en": "TAGDEMPT",
                        "name_ar": "تاقدمت"
                    }, {
                        "code": 1434,
                        "name": "MECHRAA SAFA",
                        "name_en": "MECHRAA SAFA",
                        "name_ar": "مشرع الصفا"
                    }]
                }, {
                    "code":
                    1435,
                    "name":
                    "HAMADIA",
                    "name_ar":
                    "حمادية",
                    "name_en":
                    "HAMADIA",
                    "baladyiats": [{
                        "code": 1430,
                        "name": "RECHAIGA",
                        "name_en": "RECHAIGA",
                        "name_ar": "الرشايقة"
                    }, {
                        "code": 1435,
                        "name": "HAMADIA",
                        "name_en": "HAMADIA",
                        "name_ar": "حمادية"
                    }, {
                        "code": 1440,
                        "name": "BOUGARA",
                        "name_en": "BOUGARA",
                        "name_ar": "بوقرة"
                    }]
                }],
                "adjacentWilayas": [32, 20, 29, 48, 38, 17, 3]
            }
        }]
        return cases
