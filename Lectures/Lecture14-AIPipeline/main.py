import csv
import json
import os
import time
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types
import smtplib
from email.mime.text import MIMEText

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")


def ingest_leads(filename):
    """CSV se leads padhta hai."""
    with open(filename, "r") as f:
        return list(csv.DictReader(f))


def validate_lead(lead):
    """Check karta hai ke zaroori fields moujood hain."""
    return bool(lead.get("name")) and bool(lead.get("message"))


def classify_message(text, retries=3):
    """Lecture13 ka function - message ko AI se classify karta hai."""
    prompt = f"""
    Tum ek customer support classifier ho. Neeche diye message ko classify karo.

    Message: "{text}"

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


def classify_lead(lead):
    """AI se lead ka category/urgency nikalta hai."""
    result = classify_message(lead["message"])
    if result:
        lead.update(result)
    else:
        lead["category"] = "Unknown"
        lead["urgency"] = "Low"
    return lead


def notify(subject, message, to_email):
    """Lecture12 ka function - Gmail se email bhejta hai."""
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())


def store_leads(leads, filename):
    """Processed leads ko JSON mein save karta hai."""
    with open(filename, "w") as f:
        json.dump(leads, f, indent=4)


def notify_hot_leads(leads):
    """High urgency leads ke liye email bhejta hai."""
    for lead in leads:
        if lead.get("urgency") == "High":
            notify("Hot Lead Alert", f"{lead['name']}: {lead['message']}", "yk033127@gmail.com")


def log_run(leads, filename):
    """Traceability ke liye ek text log likhta hai."""
    with open(filename, "w") as f:
        f.write(f"Run at: {datetime.now()}\n")
        f.write(f"Total leads: {len(leads)}\n")
        for lead in leads:
            f.write(f"{lead['name']} -> {lead.get('category', 'N/A')} ({lead.get('urgency', 'N/A')})\n")


# ---------- Poori Pipeline ----------
leads = ingest_leads("files/leads.csv")
valid_leads = [lead for lead in leads if validate_lead(lead)]
classified_leads = [classify_lead(lead) for lead in valid_leads]

store_leads(classified_leads, "files/leads_processed.json")
notify_hot_leads(classified_leads)
log_run(classified_leads, "files/run_log.txt")

print(f"{len(classified_leads)} leads processed.")