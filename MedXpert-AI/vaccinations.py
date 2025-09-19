vaccinations = {
    'infant': {
        'en': {
            'name': 'Infant Vaccination Schedule',
            'vaccines': [
                {
                    'name': 'BCG (Tuberculosis)',
                    'schedule': 'At birth',
                    'doses': '1 dose',
                    'importance': 'Protects against tuberculosis'
                },
                {
                    'name': 'Hepatitis B',
                    'schedule': 'At birth, 6 weeks, 14 weeks',
                    'doses': '3 doses',
                    'importance': 'Protects against Hepatitis B virus'
                },
                {
                    'name': 'OPV (Oral Polio Vaccine)',
                    'schedule': 'At birth, 6 weeks, 10 weeks, 14 weeks',
                    'doses': '4 doses',
                    'importance': 'Protects against polio'
                },
                {
                    'name': 'DPT (Diphtheria, Pertussis, Tetanus)',
                    'schedule': '6 weeks, 10 weeks, 14 weeks',
                    'doses': '3 doses',
                    'importance': 'Protects against diphtheria, pertussis, and tetanus'
                },
                {
                    'name': 'Hib (Haemophilus influenzae type b)',
                    'schedule': '6 weeks, 10 weeks, 14 weeks',
                    'doses': '3 doses',
                    'importance': 'Protects against bacterial meningitis and pneumonia'
                },
                {
                    'name': 'Rotavirus',
                    'schedule': '6 weeks, 10 weeks',
                    'doses': '2 doses',
                    'importance': 'Protects against severe diarrhea'
                },
                {
                    'name': 'PCV (Pneumococcal)',
                    'schedule': '6 weeks, 10 weeks, 14 weeks',
                    'doses': '3 doses',
                    'importance': 'Protects against pneumonia and meningitis'
                },
                {
                    'name': 'Measles',
                    'schedule': '9 months, 15 months',
                    'doses': '2 doses',
                    'importance': 'Protects against measles'
                }
            ]
        },
        'hi': {
            'name': 'शिशु टीकाकरण कार्यक्रम',
            'vaccines': [
                {
                    'name': 'बीसीजी (क्षय रोग)',
                    'schedule': 'जन्म के समय',
                    'doses': '1 खुराक',
                    'importance': 'क्षय रोग से बचाता है'
                },
                {
                    'name': 'हेपेटाइटिस बी',
                    'schedule': 'जन्म, 6 सप्ताह, 14 सप्ताह',
                    'doses': '3 खुराक',
                    'importance': 'हेपेटाइटिस बी वायरस से बचाता है'
                }
            ]
        }
    },
    'child': {
        'en': {
            'name': 'Child Vaccination Schedule (1-5 years)',
            'vaccines': [
                {
                    'name': 'DPT Booster',
                    'schedule': '15-18 months, 4-6 years',
                    'doses': '2 doses',
                    'importance': 'Booster for diphtheria, pertussis, and tetanus'
                },
                {
                    'name': 'OPV Booster',
                    'schedule': '15-18 months, 4-6 years',
                    'doses': '2 doses',
                    'importance': 'Booster for polio protection'
                },
                {
                    'name': 'MMR (Measles, Mumps, Rubella)',
                    'schedule': '15-18 months',
                    'doses': '1 dose',
                    'importance': 'Protects against measles, mumps, and rubella'
                },
                {
                    'name': 'Chickenpox (Varicella)',
                    'schedule': '15-18 months',
                    'doses': '1 dose',
                    'importance': 'Protects against chickenpox'
                },
                {
                    'name': 'Hepatitis A',
                    'schedule': '12-23 months',
                    'doses': '2 doses (6 months apart)',
                    'importance': 'Protects against Hepatitis A'
                }
            ]
        }
    },
    'adult': {
        'en': {
            'name': 'Adult Vaccination Schedule',
            'vaccines': [
                {
                    'name': 'Tdap (Tetanus, Diphtheria, Pertussis)',
                    'schedule': 'Every 10 years',
                    'doses': '1 dose every 10 years',
                    'importance': 'Protection against tetanus, diphtheria, and pertussis'
                },
                {
                    'name': 'Influenza (Flu)',
                    'schedule': 'Annually',
                    'doses': '1 dose every year',
                    'importance': 'Protection against seasonal influenza'
                },
                {
                    'name': 'Pneumococcal',
                    'schedule': '65+ years or high risk',
                    'doses': '1-2 doses based on age',
                    'importance': 'Protection against pneumonia'
                },
                {
                    'name': 'Shingles (Herpes Zoster)',
                    'schedule': '50+ years',
                    'doses': '2 doses',
                    'importance': 'Protection against shingles'
                },
                {
                    'name': 'COVID-19',
                    'schedule': 'As per government guidelines',
                    'doses': 'Primary series + boosters',
                    'importance': 'Protection against COVID-19'
                }
            ]
        }
    },
    'pregnant_women': {
        'en': {
            'name': 'Vaccination for Pregnant Women',
            'vaccines': [
                {
                    'name': 'Tdap (Tetanus, Diphtheria, Pertussis)',
                    'schedule': '27-36 weeks of pregnancy',
                    'doses': '1 dose',
                    'importance': 'Protects newborn from pertussis'
                },
                {
                    'name': 'Influenza (Flu)',
                    'schedule': 'Any time during pregnancy',
                    'doses': '1 dose annually',
                    'importance': 'Protection during pregnancy'
                }
            ]
        }
    }
}

def get_vaccination_info(age_group: str, language: str = 'en') -> dict:
    """Get vaccination information for specific age group"""
    if age_group in vaccinations and language in vaccinations[age_group]:
        return vaccinations[age_group][language]
    return None

def get_all_vaccinations(language: str = 'en') -> dict:
    """Get all vaccination schedules"""
    result = {}
    for age_group in vaccinations:
        if language in vaccinations[age_group]:
            result[age_group] = vaccinations[age_group][language]
    return result