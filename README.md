# MedXpert AI - Rural Healthcare Education Platform

A comprehensive multilingual AI chatbot designed to educate rural and semi-urban populations about preventive healthcare, disease symptoms, vaccination schedules, and outbreak alerts. Built with Python and FastAPI, integrating with government health databases for real-time information.

## 🎯 Project Description

This platform creates a multilingual AI chatbot to educate rural and semi-urban populations about preventive healthcare, disease symptoms, and vaccination schedules. The chatbot integrates with government health databases and provides real-time alerts for outbreaks, aiming to reach 80% accuracy in answering health queries and increase awareness by 20% in target communities.

## ✨ Key Features

### 🏥 Core Healthcare Features
- **Disease Information**: Comprehensive database of 10+ diseases with symptoms, prevention, and treatment
- **Vaccination Schedules**: Complete vaccination schedules for infants, children, adults, and pregnant women
- **Outbreak Alerts**: Real-time alerts about disease outbreaks with location-specific information
- **Preventive Healthcare**: Education modules on hygiene, nutrition, mental health, and sanitation

### 🤖 AI & Technology
- **AI-Powered Responses**: Advanced AI with medical knowledge for accurate, personalized health responses
- **Multilingual Support**: Communicate in 6 languages (English, Hindi, Tamil, Telugu, Urdu, Odia)
- **Conversational Memory**: Context-aware conversations for better user experience
- **Multi-Channel Access**: Available via web, WhatsApp, and SMS

### 🌍 Rural-Focused Design
- **Offline Capabilities**: Basic functionality works without internet
- **Simple Interface**: Easy-to-use design suitable for low-literacy users
- **Voice Integration**: Support for voice-based interactions
- **Local Language Support**: Content optimized for rural dialects

## Setup

1. Clone the repository
2. Install Python dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your API keys (optional - chatbot works without them):
   ```
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_phone_number
   OPENAI_API_KEY=your_openai_api_key
   PORT=3000
   ```
4. Run the server: `python server.py`
5. For development with auto-reload: `uvicorn server:app --reload`

**Note:** The chatbot will work without API keys for basic disease information. Add API keys for enhanced AI responses and SMS functionality.

## 🎯 Expected Outcomes

### 📊 Target Metrics
- **80% Query Accuracy**: Achieve 80% accuracy in answering health-related queries
- **20% Awareness Increase**: Increase health awareness by 20% in target communities
- **Multi-Channel Reach**: Accessible via WhatsApp, SMS, and web interface
- **Rural Coverage**: Reach 50,000+ users in rural and semi-urban areas within first year

### 📈 Impact Goals
- **Disease Prevention**: Reduce incidence of preventable diseases through education
- **Vaccination Coverage**: Improve vaccination rates through timely reminders
- **Health Literacy**: Increase health literacy among rural populations
- **Emergency Response**: Enable faster response to health emergencies

## 🔧 Technical Feasibility

### 🏗️ Architecture
- **NLP Framework**: Built using Python with FastAPI for robust API development
- **AI Integration**: OpenAI GPT models for intelligent conversation
- **Multi-Channel Support**: Twilio integration for WhatsApp and SMS
- **Database Integration**: APIs for government health database connectivity

### ☁️ Deployment & Scalability
- **Cloud Platform**: Deployable on AWS, Google Cloud, or Azure
- **Microservices**: Modular architecture for easy scaling
- **Load Balancing**: Handle thousands of concurrent users
- **Offline Support**: Basic functionality works without internet

### 📱 Usage Instructions

#### 🌐 Web Interface
- Open browser and go to `http://localhost:3000`
- Use quick action buttons for specific health topics
- Switch between 6 languages using the language selector
- Access vaccination schedules, outbreak alerts, and preventive care

#### 💬 WhatsApp Interface
- Message the MedXpert AI WhatsApp number
- Ask questions in your preferred language
- Receive instant responses with health information
- Get vaccination reminders and outbreak alerts

#### 📱 SMS Interface
- Send SMS to the MedXpert AI number
- Receive structured health information
- Get emergency contact information
- Access in areas with limited internet

## Disease Search Features

The chatbot can recognize and provide detailed information for these diseases:
- COVID-19
- Diabetes
- Hypertension (High Blood Pressure)
- Malaria
- Tuberculosis (TB)
- Dengue Fever
- Asthma
- Cancer
- Influenza (Flu)
- HIV/AIDS

### Example Queries:
- "What are symptoms of COVID-19?"
- "Tell me about diabetes"
- "How to prevent malaria?"
- "What is tuberculosis?"
- "Symptoms of dengue fever"

## 🔌 API Endpoints

### 💬 Communication Endpoints
- `POST /sms`: Twilio webhook for incoming SMS
- `POST /whatsapp`: Twilio webhook for WhatsApp messages
- `POST /chat`: Web chat endpoint for real-time conversation

### 📊 Health Information Endpoints
- `GET /api/languages`: Get available languages and UI translations
- `GET /api/vaccinations`: Get all vaccination schedules
- `GET /api/vaccinations/{age_group}`: Get vaccination schedule for specific age group
- `GET /api/outbreaks`: Get active outbreak information
- `GET /api/outbreaks/alerts`: Get outbreak alerts in user's language
- `GET /api/outbreaks/location/{location}`: Get outbreak risks for specific location
- `GET /api/preventive-health`: Get all preventive healthcare modules
- `GET /api/preventive-health/{category}`: Get specific preventive health category
- `GET /api/search`: Search across all health information

### 🔧 System Endpoints
- `GET /health`: Health check endpoint
- `GET /`: Serve main web interface
- `GET /style.css`: Serve CSS styles
- `GET /script.js`: Serve JavaScript functionality

## Testing

Run the application and test the endpoints manually, or create automated tests using pytest.

## Deployment

Deploy to a server (e.g., Heroku, AWS, DigitalOcean) and set the Twilio webhook URL to `https://yourdomain.com/sms`

## 📁 Project Structure

```
med/
├── server.py                    # Main FastAPI application with all endpoints
├── config.py                    # Configuration management
├── diseases.py                  # Disease information database (English)
├── diseases_multilang.py        # Multilingual disease information
├── languages.py                 # UI language configurations and translations
├── vaccinations.py              # Vaccination schedules and reminders
├── outbreaks.py                 # Outbreak alert system and location-based risks
├── preventive_health.py         # Preventive healthcare education modules
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (API keys, etc.)
├── .vscode/
│   └── launch.json              # VS Code debugging configuration
└── public/
    ├── index.html               # Main web interface with rural-friendly design
    ├── style.css                # Professional healthcare-themed CSS
    └── script.js                # Frontend JavaScript for chat functionality
```

## Technologies

- Python 3.8+
- FastAPI
- Uvicorn (ASGI server)
- Twilio Python SDK
- OpenAI Python SDK
- python-dotenv