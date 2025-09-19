hospitals_data = {
    'delhi': [
        {
            'name': 'All India Institute of Medical Sciences (AIIMS)',
            'type': 'Government Hospital',
            'specialty': 'Multi-specialty',
            'address': 'Ansari Nagar, New Delhi - 110029',
            'phone': '+91-11-26588500',
            'emergency': '+91-11-26589900',
            'email': 'info@aiims.edu',
            'services': ['Emergency Care', 'Cardiology', 'Neurology', 'Oncology', 'Pediatrics'],
            'facilities': ['24/7 Emergency', 'ICU', 'Ambulance', 'Pharmacy', 'Blood Bank'],
            'rating': 4.8,
            'distance': '0 km'
        },
        {
            'name': 'Safdarjung Hospital',
            'type': 'Government Hospital',
            'specialty': 'Multi-specialty',
            'address': 'Ansari Nagar West, New Delhi - 110029',
            'phone': '+91-11-26707444',
            'emergency': '+91-11-26707400',
            'email': 'info@safdarjunghospital.nic.in',
            'services': ['Emergency Care', 'Trauma Center', 'Maternity', 'Surgery'],
            'facilities': ['24/7 Emergency', 'NICU', 'Blood Bank', 'Diagnostic Center'],
            'rating': 4.5,
            'distance': '2 km'
        },
        {
            'name': 'Apollo Hospital Delhi',
            'type': 'Private Hospital',
            'specialty': 'Multi-specialty',
            'address': 'Mathura Road, Sarita Vihar, New Delhi - 110076',
            'phone': '+91-11-26925858',
            'emergency': '+91-11-26925801',
            'email': 'info@apollohospitals.com',
            'services': ['Cardiology', 'Oncology', 'Neurology', 'Orthopedics', 'Emergency'],
            'facilities': ['24/7 Emergency', 'ICU', 'Ambulance', 'Pharmacy', 'Cafeteria'],
            'rating': 4.7,
            'distance': '15 km'
        }
    ],
    'mumbai': [
        {
            'name': 'KEM Hospital',
            'type': 'Government Hospital',
            'specialty': 'Multi-specialty',
            'address': 'Parel, Mumbai - 400012',
            'phone': '+91-22-24136051',
            'emergency': '+91-22-24136000',
            'email': 'info@kem.edu',
            'services': ['Emergency Care', 'Maternity', 'Surgery', 'Pediatrics'],
            'facilities': ['24/7 Emergency', 'NICU', 'Blood Bank', 'Diagnostic Center'],
            'rating': 4.6,
            'distance': '0 km'
        },
        {
            'name': 'Lilavati Hospital',
            'type': 'Private Hospital',
            'specialty': 'Multi-specialty',
            'address': 'A-791, Bandra Reclamation, Bandra West, Mumbai - 400050',
            'phone': '+91-22-26751000',
            'emergency': '+91-22-26751091',
            'email': 'info@lilavatihospital.com',
            'services': ['Cardiology', 'Oncology', 'Neurology', 'Emergency'],
            'facilities': ['24/7 Emergency', 'ICU', 'Ambulance', 'Pharmacy'],
            'rating': 4.8,
            'distance': '8 km'
        }
    ],
    'chennai': [
        {
            'name': 'Stanley Medical College Hospital',
            'type': 'Government Hospital',
            'specialty': 'Multi-specialty',
            'address': 'Old Jail Road, Chennai - 600001',
            'phone': '+91-44-25281347',
            'emergency': '+91-44-25281300',
            'email': 'info@stanley.in',
            'services': ['Emergency Care', 'Maternity', 'Surgery', 'Medicine'],
            'facilities': ['24/7 Emergency', 'Blood Bank', 'Diagnostic Center'],
            'rating': 4.4,
            'distance': '0 km'
        },
        {
            'name': 'Apollo Hospitals Chennai',
            'type': 'Private Hospital',
            'specialty': 'Multi-specialty',
            'address': '21, Greams Lane, Off Greams Road, Chennai - 600006',
            'phone': '+91-44-28290200',
            'emergency': '+91-44-28293333',
            'email': 'info@apollohospitalschennai.com',
            'services': ['Cardiology', 'Oncology', 'Neurology', 'Emergency'],
            'facilities': ['24/7 Emergency', 'ICU', 'Ambulance', 'Pharmacy'],
            'rating': 4.7,
            'distance': '5 km'
        }
    ],
    'kolkata': [
        {
            'name': 'SSKM Hospital',
            'type': 'Government Hospital',
            'specialty': 'Multi-specialty',
            'address': '242, AJC Bose Road, Kolkata - 700020',
            'phone': '+91-33-22041101',
            'emergency': '+91-33-22041100',
            'email': 'info@sskm.in',
            'services': ['Emergency Care', 'Surgery', 'Medicine', 'Pediatrics'],
            'facilities': ['24/7 Emergency', 'Blood Bank', 'Diagnostic Center'],
            'rating': 4.3,
            'distance': '0 km'
        }
    ],
    'bangalore': [
        {
            'name': 'Victoria Hospital',
            'type': 'Government Hospital',
            'specialty': 'Multi-specialty',
            'address': 'Fort, Bangalore - 560002',
            'phone': '+91-80-26703100',
            'emergency': '+91-80-26703191',
            'email': 'info@victoriahospital.in',
            'services': ['Emergency Care', 'Maternity', 'Surgery', 'Medicine'],
            'facilities': ['24/7 Emergency', 'Blood Bank', 'Diagnostic Center'],
            'rating': 4.5,
            'distance': '0 km'
        },
        {
            'name': 'Manipal Hospital',
            'type': 'Private Hospital',
            'specialty': 'Multi-specialty',
            'address': '98, HAL Airport Road, Bangalore - 560017',
            'phone': '+91-80-25024444',
            'emergency': '+91-80-25024400',
            'email': 'info@manipalhospitals.com',
            'services': ['Cardiology', 'Oncology', 'Neurology', 'Emergency'],
            'facilities': ['24/7 Emergency', 'ICU', 'Ambulance', 'Pharmacy'],
            'rating': 4.6,
            'distance': '12 km'
        }
    ]
}

emergency_services = {
    'ambulance': {
        'national': '108',
        'description': 'Free ambulance service available 24/7 across India'
    },
    'police': {
        'national': '100',
        'description': 'Emergency police services'
    },
    'fire': {
        'national': '101',
        'description': 'Fire emergency services'
    },
    'women_helpline': {
        'national': '1091',
        'description': 'Women helpline for emergency assistance'
    },
    'child_helpline': {
        'national': '1098',
        'description': 'Child helpline for emergency assistance'
    },
    'mental_health': {
        'national': '1800-121-4567',
        'description': 'Mental health helpline'
    }
}

essential_services = {
    'blood_banks': [
        {
            'name': 'Indian Red Cross Society',
            'phone': '+91-11-23716441',
            'services': ['Blood donation', 'Blood storage', 'Emergency supply']
        },
        {
            'name': 'Rotary Blood Bank',
            'phone': '+91-22-2409-1111',
            'services': ['Blood donation camps', 'Component separation', 'Emergency services']
        }
    ],
    'pharmacies': [
        {
            'name': '24/7 Pharmacy Network',
            'description': 'Emergency medicine delivery service',
            'contact': 'Local pharmacy numbers vary by location'
        }
    ],
    'diagnostic_centers': [
        {
            'name': 'Government Diagnostic Centers',
            'description': 'Affordable diagnostic services',
            'services': ['Blood tests', 'X-rays', 'Ultrasound', 'ECG']
        }
    ],
    'medical_stores': [
        {
            'name': 'Government Medical Stores',
            'description': 'Essential medicines at subsidized rates',
            'services': ['Generic medicines', 'Vaccines', 'Medical supplies']
        }
    ]
}

def get_hospitals_by_location(location: str) -> list:
    """Get hospitals for a specific location"""
    location_lower = location.lower()
    for city in hospitals_data:
        if city in location_lower or location_lower in city:
            return hospitals_data[city]
    return []

def get_emergency_services() -> dict:
    """Get emergency services information"""
    return emergency_services

def get_essential_services() -> dict:
    """Get essential services information"""
    return essential_services

def search_hospitals(query: str) -> list:
    """Search hospitals by name, specialty, or services"""
    query_lower = query.lower()
    results = []

    for city_hospitals in hospitals_data.values():
        for hospital in city_hospitals:
            if (query_lower in hospital['name'].lower() or
                query_lower in hospital['specialty'].lower() or
                any(query_lower in service.lower() for service in hospital['services'])):
                results.append(hospital)

    return results