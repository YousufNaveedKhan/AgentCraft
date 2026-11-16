
from google import genai
from google.genai import types
import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Primary + Fallback models
MODELS = [
    "gemini-3.8-flash",
    "gemini-3.5-flash-lite"
]


def get_weather(city: str):
    """Diye gaye shehar ka current temperature return karta hai."""

    geo = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city},
        timeout=10
    ).json()

    if not geo.get("results"):
        return f"{city} ka location nahi mila."

    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]

    weather = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        },
        timeout=10
    ).json()

    return weather["current_weather"]["temperature"]


def calculate_shipping(weight_kg: float):
    """Weight ke hisaab se shipping cost calculate karta hai."""

    if weight_kg <= 1:
        return 200
    elif weight_kg <= 5:
        return 500
    else:
        return 1000


def generate_with_fallback(contents, config=None, retries=2):
    """Primary model fail hone par fallback model use karta hai."""

    for model in MODELS:

        print(f"\nTrying model: {model}")

        for attempt in range(retries):

            try:
                response = client.models.generate_content(
                    model=model,
                    contents=contents,
                    config=config
                )

                print(f"Successfully used: {model}")
                return response

            except Exception as e:

                print(
                    f"{model} failed "
                    f"(Attempt {attempt + 1}): {e}"
                )

                # Retry only for temporary server/rate-limit errors
                status = getattr(e, "code", None)

                if status in [429, 500, 502, 503, 504]:
                    time.sleep(3 * (attempt + 1))
                    continue

                # Invalid model or other permanent error:
                # Move directly to the next model.
                break

        print(f"Switching from {model} to next model...")

    return None


response = generate_with_fallback(
    contents="Mujhe Karachi ka weather batao.",
    config=types.GenerateContentConfig(
        tools=[get_weather, calculate_shipping]
    )
)

if response:
    print("\nAI Response:")
    print(response.text)
else:
    print("\nAll models failed. Response nahi mil saka!")
