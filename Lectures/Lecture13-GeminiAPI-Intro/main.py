from google import genai
from google.genai import types
import os 
import time
import json
from dotenv import load_dotenv 

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def classify_message(text, retries=3):
    """Message ko AI se classify karta hai."""
    prompt = f"""
    Tum ek customer support classifier ho.
    Neche diye huwe message ko classify karo.

    Message: {text}
    
    Sirf is JSON format mein jawab do:
    {{"category": "...", "urgency": "High/Medium/Low", "reason": "..."}}
    """

    for attempt in range(retries):
        try:
            response = client.models.generate_content(
               model="gemini-3.8-flash", 
               contents=prompt, 
               config=types.GenerateContentConfig(response_mime_type="application/json") 
            )
            return json.loads(response.text)
        except Exception as e:
            print(f"Attempt {attempt + 1} fail hui: {e}")
            time.sleep(2)

        return None

result = classify_message("Mera order 5 din se nahin aaya hai.. bohot zaroori hai!")
print(f"[{result["urgency"]}] {result["category"]} --- {result["reason"]}")