from google import genai
from google.genai import types
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_current_time():
    """Current date and time return karta hai."""
    return datetime.now().isoformat()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Abhi ka exact time btao?",
    config=types.GenerateContentConfig(tools=[get_current_time])
)

print(response.text)