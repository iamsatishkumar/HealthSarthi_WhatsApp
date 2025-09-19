import datetime
from typing import List, Dict, Any

# Simulated outbreak data - in real implementation, this would come from government APIs
outbreaks = {
    'active': [
        {
            'id': 'OUT-2025-001',
            'disease': 'Dengue',
            'location': 'Delhi, India',
            'severity': 'High',
            'cases': 1250,
            'start_date': '2025-01-15',
            'status': 'Active',
            'precautions': [
                'Use mosquito repellents',
                'Wear long-sleeved clothing',
                'Eliminate standing water',
                'Use mosquito nets'
            ],
            'affected_areas': ['Delhi', 'Gurgaon', 'Noida']
        },
        {
            'id': 'OUT-2025-002',
            'disease': 'Malaria',
            'location': 'Odisha, India',
            'severity': 'Medium',
            'cases': 450,
            'start_date': '2025-02-01',
            'status': 'Active',
            'precautions': [
                'Use mosquito nets',
                'Take antimalarial medication',
                'Wear protective clothing',
                'Avoid outdoor activities at dawn/dusk'
            ],
            'affected_areas': ['Koraput', 'Malkangiri', 'Nabarangpur']
        }
    ],
    'resolved': [
        {
            'id': 'OUT-2024-015',
            'disease': 'COVID-19',
            'location': 'Global',
            'severity': 'Low',
            'cases': 0,
            'start_date': '2024-12-01',
            'end_date': '2025-01-15',
            'status': 'Resolved',
            'precautions': []
        }
    ]
}

def get_active_outbreaks() -> List[Dict[str, Any]]:
    """Get all active outbreaks"""
    return outbreaks['active']

def get_outbreaks_by_location(location: str) -> List[Dict[str, Any]]:
    """Get outbreaks for specific location"""
    location_lower = location.lower()
    result = []

    for outbreak in outbreaks['active']:
        if any(area.lower() in location_lower or location_lower in area.lower()
               for area in outbreak['affected_areas']):
            result.append(outbreak)

    return result

def get_outbreaks_by_disease(disease: str) -> List[Dict[str, Any]]:
    """Get outbreaks for specific disease"""
    disease_lower = disease.lower()
    result = []

    for outbreak in outbreaks['active']:
        if disease_lower in outbreak['disease'].lower():
            result.append(outbreak)

    return result

def get_outbreak_alerts(language: str = 'en') -> str:
    """Generate outbreak alert message"""
    active_outbreaks = get_active_outbreaks()

    if not active_outbreaks:
        if language == 'hi':
            return "वर्तमान में कोई सक्रिय महामारी नहीं है।"
        elif language == 'ta':
            return "தற்போது செயலில் உள்ள எந்தவொரு வெடிப்பும் இல்லை."
        elif language == 'te':
            return "ప్రస్తుతం ఎటువంటి చురుకైన వ్యాధి వెల్లువ లేదు."
        else:
            return "No active outbreaks currently."

    alert_message = ""
    if language == 'en':
        alert_message = f"🚨 HEALTH ALERT: {len(active_outbreaks)} active outbreak(s) reported:\n\n"
        for outbreak in active_outbreaks:
            alert_message += f"• {outbreak['disease']} in {outbreak['location']}\n"
            alert_message += f"  Severity: {outbreak['severity']} ({outbreak['cases']} cases)\n"
            alert_message += f"  Precautions: {', '.join(outbreak['precautions'][:2])}...\n\n"
    elif language == 'hi':
        alert_message = f"🚨 स्वास्थ्य चेतावनी: {len(active_outbreaks)} सक्रिय महामारी की सूचना:\n\n"
        for outbreak in active_outbreaks:
            alert_message += f"• {outbreak['location']} में {outbreak['disease']}\n"
            alert_message += f"  गंभीरता: {outbreak['severity']} ({outbreak['cases']} मामले)\n"
            alert_message += f"  सावधानियाँ: {', '.join(outbreak['precautions'][:2])}...\n\n"

    return alert_message

def check_location_risk(location: str, language: str = 'en') -> str:
    """Check if location has any outbreak risks"""
    location_outbreaks = get_outbreaks_by_location(location)

    if not location_outbreaks:
        if language == 'hi':
            return f"{location} में वर्तमान में कोई महामारी जोखिम नहीं है।"
        elif language == 'ta':
            return f"{location} இல் தற்போது எந்த வெடிப்பு அபாயமும் இல்லை."
        elif language == 'te':
            return f"{location} లో ప్రస్తుతం ఎటువంటి వ్యాధి వెల్లువ ప్రమాదం లేదు."
        else:
            return f"No current outbreak risks in {location}."

    risk_message = ""
    if language == 'en':
        risk_message = f"⚠️ RISK ALERT for {location}:\n\n"
        for outbreak in location_outbreaks:
            risk_message += f"• {outbreak['disease']} outbreak active\n"
            risk_message += f"  Cases: {outbreak['cases']}\n"
            risk_message += f"  Key precautions:\n"
            for precaution in outbreak['precautions'][:3]:
                risk_message += f"    - {precaution}\n"
            risk_message += "\n"
    elif language == 'hi':
        risk_message = f"⚠️ {location} के लिए जोखिम चेतावनी:\n\n"
        for outbreak in location_outbreaks:
            risk_message += f"• {outbreak['disease']} महामारी सक्रिय\n"
            risk_message += f"  मामले: {outbreak['cases']}\n"
            risk_message += f"  मुख्य सावधानियाँ:\n"
            for precaution in outbreak['precautions'][:3]:
                risk_message += f"    - {precaution}\n"
            risk_message += "\n"

    return risk_message