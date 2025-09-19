preventive_health_modules = {
    'hygiene': {
        'en': {
            'title': 'Personal Hygiene and Sanitation',
            'content': {
                'hand_washing': {
                    'title': 'Hand Washing',
                    'description': 'Wash hands with soap and water for 20 seconds',
                    'steps': [
                        'Wet hands with clean water',
                        'Apply soap and rub hands together',
                        'Scrub all parts for 20 seconds',
                        'Rinse with clean water',
                        'Dry with clean cloth or air dry'
                    ],
                    'importance': 'Prevents spread of diseases like diarrhea, flu, and COVID-19'
                },
                'oral_hygiene': {
                    'title': 'Oral Hygiene',
                    'description': 'Brush teeth twice daily and use mouthwash',
                    'tips': [
                        'Brush teeth for 2 minutes twice daily',
                        'Use fluoride toothpaste',
                        'Clean tongue daily',
                        'Visit dentist every 6 months',
                        'Avoid sugary foods and drinks'
                    ]
                },
                'sanitation': {
                    'title': 'Environmental Sanitation',
                    'description': 'Keep surroundings clean to prevent diseases',
                    'practices': [
                        'Dispose waste properly',
                        'Keep water containers covered',
                        'Clean toilets regularly',
                        'Eliminate mosquito breeding sites',
                        'Maintain clean cooking areas'
                    ]
                }
            }
        },
        'hi': {
            'title': 'व्यक्तिगत स्वच्छता और सफाई',
            'content': {
                'hand_washing': {
                    'title': 'हाथ धोना',
                    'description': 'साबुन और पानी से 20 सेकंड तक हाथ धोएं',
                    'steps': [
                        'साफ पानी से हाथ गीला करें',
                        'साबुन लगाएं और हाथ रगड़ें',
                        '20 सेकंड तक सभी भाग साफ करें',
                        'साफ पानी से धोएं',
                        'साफ कपड़े से या हवा में सुखाएं'
                    ]
                }
            }
        }
    },
    'nutrition': {
        'en': {
            'title': 'Nutrition and Healthy Eating',
            'content': {
                'balanced_diet': {
                    'title': 'Balanced Diet',
                    'description': 'Eat variety of foods for good health',
                    'food_groups': {
                        'cereals': 'Rice, wheat, millets - 6-11 servings',
                        'vegetables': 'Leafy greens, carrots, tomatoes - 3-5 servings',
                        'fruits': 'Seasonal fruits - 2-4 servings',
                        'proteins': 'Eggs, fish, legumes, nuts - 2-3 servings',
                        'dairy': 'Milk, yogurt, cheese - 2-3 servings'
                    }
                },
                'micronutrients': {
                    'title': 'Important Micronutrients',
                    'vitamins': {
                        'vitamin_a': 'For vision and immunity (carrots, spinach)',
                        'vitamin_c': 'For immunity (citrus fruits, tomatoes)',
                        'vitamin_d': 'For bones (sunlight, fortified foods)',
                        'iron': 'For blood (leafy greens, legumes)',
                        'iodine': 'For thyroid (iodized salt)'
                    }
                }
            }
        }
    },
    'maternal_child_health': {
        'en': {
            'title': 'Maternal and Child Health',
            'content': {
                'antenatal_care': {
                    'title': 'Antenatal Care',
                    'visits': [
                        'First visit: Before 12 weeks',
                        'Second visit: 16-20 weeks',
                        'Third visit: 28-32 weeks',
                        'Fourth visit: 36 weeks onwards'
                    ],
                    'importance': 'Monitor mother and baby health, detect complications early'
                },
                'breastfeeding': {
                    'title': 'Breastfeeding',
                    'benefits': [
                        'Provides perfect nutrition for baby',
                        'Boosts baby\'s immunity',
                        'Helps mother recover after delivery',
                        'Reduces risk of infections',
                        'Promotes bonding between mother and baby'
                    ],
                    'guidelines': 'Exclusive breastfeeding for first 6 months, continue up to 2 years'
                }
            }
        }
    },
    'mental_health': {
        'en': {
            'title': 'Mental Health and Well-being',
            'content': {
                'stress_management': {
                    'title': 'Stress Management',
                    'techniques': [
                        'Deep breathing exercises',
                        'Regular physical activity',
                        'Adequate sleep (7-8 hours)',
                        'Healthy eating habits',
                        'Talking to friends/family',
                        'Meditation or yoga'
                    ]
                },
                'mental_health_myths': {
                    'title': 'Common Myths About Mental Health',
                    'myths': [
                        'Mental illness is rare - FACT: 1 in 4 people experience mental health issues',
                        'Mental illness is a sign of weakness - FACT: It\'s a medical condition like any other',
                        'People with mental illness are dangerous - FACT: Most are not violent',
                        'Mental illness cannot be treated - FACT: Many can be effectively managed'
                    ]
                }
            }
        }
    },
    'environmental_health': {
        'en': {
            'title': 'Environmental Health',
            'content': {
                'water_safety': {
                    'title': 'Safe Drinking Water',
                    'sources': [
                        'Boil water for 1 minute',
                        'Use water filters',
                        'Store in clean containers',
                        'Test water quality regularly',
                        'Use chlorine tablets when needed'
                    ]
                },
                'waste_management': {
                    'title': 'Waste Management',
                    'practices': [
                        'Segregate waste (wet/dry)',
                        'Dispose biomedical waste properly',
                        'Compost organic waste',
                        'Recycle plastics and paper',
                        'Avoid burning waste'
                    ]
                }
            }
        }
    }
}

def get_preventive_health_info(category: str, language: str = 'en') -> dict:
    """Get preventive health information for specific category"""
    if category in preventive_health_modules and language in preventive_health_modules[category]:
        return preventive_health_modules[category][language]
    return None

def get_all_preventive_health(language: str = 'en') -> dict:
    """Get all preventive health modules"""
    result = {}
    for category in preventive_health_modules:
        if language in preventive_health_modules[category]:
            result[category] = preventive_health_modules[category][language]
    return result

def search_preventive_health(query: str, language: str = 'en') -> list:
    """Search preventive health content for relevant information"""
    query_lower = query.lower()
    results = []

    for category, lang_data in preventive_health_modules.items():
        if language in lang_data:
            category_data = lang_data[language]

            # Search in title
            if query_lower in category_data['title'].lower():
                results.append({
                    'type': 'category',
                    'category': category,
                    'title': category_data['title'],
                    'content': category_data
                })

            # Search in content
            if 'content' in category_data:
                for subtopic, subcontent in category_data['content'].items():
                    if query_lower in subcontent.get('title', '').lower() or \
                       query_lower in subcontent.get('description', '').lower():
                        results.append({
                            'type': 'subtopic',
                            'category': category,
                            'subtopic': subtopic,
                            'title': subcontent['title'],
                            'content': subcontent
                        })

    return results