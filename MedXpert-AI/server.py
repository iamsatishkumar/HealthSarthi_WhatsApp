from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI
import os
from typing import Optional
from config import config
from diseases import diseases
from diseases_multilang import diseases_multilang
from languages import languages
from vaccinations import get_vaccination_info, get_all_vaccinations
from outbreaks import get_outbreak_alerts, check_location_risk, get_active_outbreaks
from preventive_health import get_preventive_health_info, get_all_preventive_health, search_preventive_health
from hospitals import get_hospitals_by_location, get_emergency_services, get_essential_services, search_hospitals, hospitals_data

app = FastAPI(title="MedXpert AI", description="Professional healthcare chatbot with AI and SMS support")

# Configure UTF-8 encoding for responses
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# Add CORS middleware
app.middleware("http")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files
from fastapi.responses import FileResponse
import os

@app.get("/style.css")
async def get_css():
    return FileResponse("public/style.css", media_type="text/css")

@app.get("/script.js")
async def get_js():
    return FileResponse("public/script.js", media_type="application/javascript")

# Twilio setup
twilio_client = None
if config.twilio['account_sid'] and config.twilio['account_sid'] != 'your_twilio_account_sid' and \
   config.twilio['auth_token'] and config.twilio['auth_token'] != 'your_twilio_auth_token':
    from twilio.rest import Client
    twilio_client = Client(config.twilio['account_sid'], config.twilio['auth_token'])

# OpenAI setup
openai_client = None
if config.openai['api_key'] and config.openai['api_key'] != 'your_openai_api_key':
    openai_client = OpenAI(api_key=config.openai['api_key'])

# In-memory storage for conversation history
conversation_history = {}

# Localized labels
localized_labels = {
    'symptoms': {
        'en': 'Symptoms',
        'hi': 'लक्षण',
        'ta': 'அறிகுறிகள்',
        'te': 'లక్షణాలు',
        'ur': 'علامات',
        'or': 'ଲକ୍ଷଣ'
    },
    'prevention': {
        'en': 'Prevention',
        'hi': 'रोकथाम',
        'ta': 'தடுப்பு',
        'te': 'నివారణ',
        'ur': 'بچاؤ',
        'or': 'ନିବାରଣ'
    },
    'treatment': {
        'en': 'Treatment',
        'hi': 'उपचार',
        'ta': 'சிகிச்சை',
        'te': 'చికిత్స',
        'ur': 'علاج',
        'or': 'ଚିକିତ୍ସା'
    },
    'awareness': {
        'en': 'Awareness',
        'hi': 'जागरूकता',
        'ta': 'விழிப்புணர்வு',
        'te': 'అవగాహన',
        'ur': 'آگاہی',
        'or': 'ସଚେତନତା'
    }
}

def get_localized_label(key: str, language: str = 'en') -> str:
    """Get localized label for a given key and language"""
    return localized_labels.get(key, {}).get(language, localized_labels.get(key, {}).get('en', key))

def get_language_name(language: str) -> str:
    """Get full language name from code"""
    names = {
        'hi': 'Hindi',
        'ta': 'Tamil',
        'te': 'Telugu',
        'ur': 'Urdu',
        'or': 'Odia'
    }
    return names.get(language, 'English')

def get_fallback_message(msg_type: str, language: str = 'en') -> str:
    """Get fallback messages for different types and languages"""
    messages = {
        'error': {
            'en': 'Sorry, I am unable to respond right now. Please try again later.',
            'hi': 'क्षमा करें, मैं अभी जवाब नहीं दे सकता। कृपया बाद में पुनः प्रयास करें।',
            'ta': 'மன்னிக்கவும், என்னால் இப்போது பதிலளிக்க முடியவில்லை. தயவுசெய்து பின்னர் மீண்டும் முயற்சிக்கவும்.',
            'te': 'క్షమించండి, నేను ఇప్పుడు సమాధానం ఇవ్వలేకపోతున్నాను. దయచేసి తర్వాత మళ్లీ ప్రయత్నించండి.',
            'ur': 'معذرت، میں ابھی جواب نہیں دے سکتا۔ براہ کرم بعد میں دوبارہ کوشش کریں۔',
            'or': 'ଦୁଃଖିତ, ମୁଁ ବର୍ତ୍ତମାନ ଉତ୍ତର ଦେଇପାରୁନାହିଁ। ଦୟାକରି ପରେ ପୁନର୍ବାର ଚେଷ୍ଟା କରନ୍ତୁ।'
        },
        'general': {
            'en': 'I\'m a health chatbot with information about various diseases. I can provide details about symptoms, prevention, treatment, and awareness for diseases like COVID-19, diabetes, malaria, and more. What specific health topic would you like to know about?',
            'hi': 'मैं विभिन्न बीमारियों की जानकारी वाला एक स्वास्थ्य चैटबॉट हूं। मैं कोविड-19, मधुमेह, मलेरिया आदि जैसी बीमारियों के लक्षण, रोकथाम, उपचार और जागरूकता के बारे में विवरण प्रदान कर सकता हूं। आप किस विशिष्ट स्वास्थ्य विषय के बारे में जानना चाहते हैं?',
            'ta': 'நான் பல்வேறு நோய்கள் பற்றிய தகவல்களைக் கொண்ட ஒரு சுகாதார சாட்போட். கோவிட்-19, நீரிழிவு, மலேரியா போன்ற நோய்களின் அறிகுறிகள், தடுப்பு, சிகிச்சை மற்றும் விழிப்புணர்வு பற்றிய விவரங்களை என்னால் வழங்க முடியும். நீங்கள் எந்த குறிப்பிட்ட சுகாதார தலைப்பைப் பற்றி அறிய விரும்புகிறீர்கள்?',
            'te': 'నేను వివిధ వ్యాధుల గురించి సమాచారం కలిగిన ఆరోగ్య చాట్‌బాట్. కోవిడ్-19, మధుమేహం, మలేరియా వంటి వ్యాధుల లక్షణాలు, నివారణ, చికిత్స మరియు అవగాహన గురించి వివరాలు అందించగలను. మీరు ఏ నిర్దిష్ట ఆరోగ్య అంశం గురించి తెలుసుకోవాలనుకుంటున్నారు?',
            'ur': 'میں مختلف بیماریوں کی معلومات رکھنے والا ایک صحت چیٹ بوٹ ہوں۔ میں کوویڈ-19، ذیابیطس، ملیریا جیسی بیماریوں کی علامات، بچاؤ، علاج اور آگاہی کے بارے میں تفصیلات فراہم کر سکتا ہوں۔ آپ کس مخصوص صحت کے موضوع کے بارے میں جاننا چاہتے ہیں؟',
            'or': 'ମୁଁ ବିଭିନ୍ନ ରୋଗ ବିଷୟରେ ସୂଚନା ସହିତ ଏକ ସ୍ୱାସ୍ଥ୍ୟ ଚାଟବଟ୍। ମୁଁ କୋଭିଡ୍-19, ମଧୁମେହ, ମ୍ୟାଲେରିଆ ଭଳି ରୋଗର ଲକ୍ଷଣ, ନିବାରଣ, ଚିକିତ୍ସା ଏବଂ ସଚେତନତା ବିଷୟରେ ବିବରଣୀ ପ୍ରଦାନ କରିପାରିବି। ଆପଣ କେଉଁ ନିର୍ଦ୍ଦିଷ୍ଟ ସ୍ୱାସ୍ଥ୍ୟ ବିଷୟ ବିଷୟରେ ଜାଣିବାକୁ ଚାହାଁନ୍ତି?'
        }
    }

    return messages.get(msg_type, {}).get(language, messages.get(msg_type, {}).get('en', 'Sorry, I cannot respond right now.'))

def get_disease_info(message: str, language: str = 'en') -> dict:
    """Check if message contains disease keywords and return information"""
    lower_message = message.lower()

    # Check for disease keywords in multilingual database
    for key in diseases_multilang:
        disease_data = diseases_multilang[key]

        # Check if disease exists in requested language
        if language not in disease_data:
            continue

        disease = disease_data[language]
        english_disease = diseases.get(key, {})
        keywords = english_disease.get('keywords', [key])

        for keyword in keywords:
            if keyword.lower() in lower_message:
                return {
                    'found': True,
                    'response': f"**{disease['name']}**\n\n" +
                               f"**Symptoms:** {disease['symptoms']}\n\n" +
                               f"**Prevention:** {disease['prevention']}\n\n" +
                               f"**Treatment:** {disease['treatment']}\n\n" +
                               f"**Awareness:** {disease['awareness']}"
                }

    return {'found': False, 'response': None}

async def get_ai_response(message: str, user_id: str, language: str = 'en') -> str:
    """Get AI response for user message"""
    history = conversation_history.get(user_id, [])
    history.append({'role': 'user', 'content': message})

    # Check for disease-specific queries first
    disease_info = get_disease_info(message, language)

    if disease_info['found']:
        # Return structured disease information
        history.append({'role': 'assistant', 'content': disease_info['response']})
        conversation_history[user_id] = history
        try:
            print(f"Disease info response for {user_id}: {disease_info['response']}")
        except UnicodeEncodeError:
            print(f"Disease info response for {user_id}: [Response contains special characters]")
        return disease_info['response']

    # For general queries, use AI if available
    if openai_client:
        system_message = f"You are a public health chatbot providing information on diseases and health awareness. Respond in {get_language_name(language) if language != 'en' else 'English'}. Keep responses informative, accurate, and concise. Focus on prevention, symptoms, and general advice. If asked about specific diseases, suggest consulting healthcare professionals."

        try:
            completion = openai_client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'system', 'content': system_message},
                    *history
                ],
                max_tokens=200,
            )

            ai_response = completion.choices[0].message.content
            history.append({'role': 'assistant', 'content': ai_response})
            conversation_history[user_id] = history

            try:
                print(f"AI Response for {user_id}: {ai_response}")
            except UnicodeEncodeError:
                print(f"AI Response for {user_id}: [Response contains special characters]")
            return ai_response
        except Exception as e:
            print(f"Error getting AI response: {e}")
            return get_fallback_message('error', language)
    else:
        # Fallback response when AI is not available
        fallback_response = get_fallback_message('general', language)
        history.append({'role': 'assistant', 'content': fallback_response})
        conversation_history[user_id] = history
        try:
            print(f"Fallback response for {user_id}: {fallback_response}")
        except UnicodeEncodeError:
            print(f"Fallback response for {user_id}: [Response contains special characters]")
        return fallback_response

# API Endpoints

@app.post('/sms')
async def sms_webhook(
    From: str = Form(...),
    Body: str = Form(...)
):
    """Twilio SMS webhook endpoint"""
    incoming_message = Body
    from_number = From

    print(f"Received SMS from {from_number}: {incoming_message}")

    ai_response = await get_ai_response(incoming_message, from_number)

    # Create TwiML response
    response = MessagingResponse()
    response.message(ai_response)

    return HTMLResponse(content=str(response), media_type='text/xml')

@app.post('/whatsapp')
async def whatsapp_webhook(
    From: str = Form(...),
    Body: str = Form(...)
):
    """Twilio WhatsApp webhook endpoint"""
    incoming_message = Body
    from_number = From

    print(f"Received WhatsApp from {from_number}: {incoming_message}")

    ai_response = await get_ai_response(incoming_message, from_number)

    # Create TwiML response for WhatsApp
    response = MessagingResponse()
    response.message(ai_response)

    return HTMLResponse(content=str(response), media_type='text/xml')

@app.post('/chat')
async def web_chat(request: Request):
    """Web chat endpoint"""
    try:
        data = await request.json()
        message = data.get('message')
        user_id = data.get('userId', 'web-user')
        language = data.get('language', 'en')

        if not message:
            raise HTTPException(status_code=400, detail="Message is required")

        print(f"Received web chat from {user_id} in {language}: {message}")

        ai_response = await get_ai_response(message, user_id, language)
        return JSONResponse(content={'response': ai_response})

    except Exception as e:
        print(f"Error in web chat: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get('/api/languages')
async def get_languages():
    """Get available languages"""
    return JSONResponse(content=languages)

@app.get('/api/vaccinations')
async def get_vaccinations_endpoint(language: str = 'en'):
    """Get vaccination schedules"""
    vaccinations_data = get_all_vaccinations(language)
    return JSONResponse(content=vaccinations_data)

@app.get('/api/vaccinations/{age_group}')
async def get_vaccination_by_age(age_group: str, language: str = 'en'):
    """Get vaccination schedule for specific age group"""
    vaccination_data = get_vaccination_info(age_group, language)
    if vaccination_data:
        return JSONResponse(content=vaccination_data)
    return JSONResponse(content={'error': 'Age group not found'}, status_code=404)

@app.get('/api/outbreaks')
async def get_outbreaks_endpoint():
    """Get active outbreak information"""
    outbreaks_data = get_active_outbreaks()
    return JSONResponse(content=outbreaks_data)

@app.get('/api/outbreaks/alerts')
async def get_outbreak_alerts_endpoint(language: str = 'en'):
    """Get outbreak alerts"""
    alerts = get_outbreak_alerts(language)
    return JSONResponse(content={'alerts': alerts})

@app.get('/api/outbreaks/location/{location}')
async def get_outbreaks_by_location_endpoint(location: str, language: str = 'en'):
    """Get outbreak information for specific location"""
    risk_info = check_location_risk(location, language)
    return JSONResponse(content={'location': location, 'risk_info': risk_info})

@app.get('/api/preventive-health')
async def get_preventive_health_endpoint(language: str = 'en'):
    """Get all preventive health modules"""
    health_data = get_all_preventive_health(language)
    return JSONResponse(content=health_data)

@app.get('/api/preventive-health/{category}')
async def get_preventive_health_category(category: str, language: str = 'en'):
    """Get preventive health information for specific category"""
    health_data = get_preventive_health_info(category, language)
    if health_data:
        return JSONResponse(content=health_data)
    return JSONResponse(content={'error': 'Category not found'}, status_code=404)

@app.get('/api/search')
async def search_health_info(query: str, language: str = 'en'):
    """Search across all health information"""
    results = {
        'vaccinations': [],
        'preventive_health': search_preventive_health(query, language),
        'diseases': [],
        'hospitals': search_hospitals(query)
    }

    # Search vaccinations
    if 'vaccin' in query.lower() or 'टीका' in query.lower():
        results['vaccinations'] = get_all_vaccinations(language)

    return JSONResponse(content=results)

@app.get('/api/hospitals')
async def get_hospitals(location: str = None):
    """Get hospitals by location"""
    if location:
        hospitals = get_hospitals_by_location(location)
    else:
        # Return all hospitals
        hospitals = []
        for city_hospitals in hospitals_data.values():
            hospitals.extend(city_hospitals)
    return JSONResponse(content=hospitals)

@app.get('/api/emergency-services')
async def get_emergency_services_endpoint():
    """Get emergency services information"""
    services = get_emergency_services()
    return JSONResponse(content=services)

@app.get('/api/essential-services')
async def get_essential_services_endpoint():
    """Get essential services information"""
    services = get_essential_services()
    return JSONResponse(content=services)

@app.get('/api/hospitals/search')
async def search_hospitals_endpoint(query: str):
    """Search hospitals by name, specialty, or services"""
    results = search_hospitals(query)
    return JSONResponse(content=results)

@app.get('/')
async def root():
    """Serve the main HTML page"""
    with open('public/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    return HTMLResponse(content=content)

@app.get('/health')
async def health_check():
    """Health check endpoint"""
    return JSONResponse(content={
        'status': 'OK',
        'message': 'Chatbot is running'
    })

if __name__ == '__main__':
    uvicorn.run(
        'server:app',
        host='127.0.0.1',
        port=config.server['port'],
        reload=True
    )