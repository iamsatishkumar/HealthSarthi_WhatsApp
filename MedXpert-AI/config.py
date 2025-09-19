import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.twilio = {
            'account_sid': os.getenv('TWILIO_ACCOUNT_SID'),
            'auth_token': os.getenv('TWILIO_AUTH_TOKEN'),
            'phone_number': os.getenv('TWILIO_PHONE_NUMBER'),
        }
        self.openai = {
            'api_key': os.getenv('OPENAI_API_KEY'),
        }
        self.server = {
            'port': int(os.getenv('PORT', 3000)),
        }

config = Config()