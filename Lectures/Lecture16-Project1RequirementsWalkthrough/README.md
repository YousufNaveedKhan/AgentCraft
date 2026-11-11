# Lecture 16 — Project1 Requirements Walkthrough

Yeh koi naya coding topic nahi hai — aaj **Project1 (Smart Lead Intake & AI Triage Pipeline)** ki requirements poori tafseel se samjhayi jayengi, taake agli demo day se pehle har student ko bilkul clear ho ke kya banana hai. Poora detailed brief repo mein yahan bhi maujood hai: [`Projects/Project1-LeadTriagePipeline/README.md`](../../Projects/Project1-LeadTriagePipeline/README.md).

## Aaj Ka Maqsad
Lectures 09, 11, 12, 13, 14 mein Project1 ke tukde ban chuke hain, lekin kabhi ek jagah poori requirement list clearly nahi di gayi thi. Aaj woh gap band hoga.

## Walkthrough Kaise Chalega
1. Har requirement ek-ek kar ke bolni hai
2. Har requirement ke sath batana hai **yeh kis lecture mein already bana chuka hai** (taake students ko pata chale ke yeh unke liye naya kaam nahi, sirf organize karna hai)
3. Sawalat lena har point ke baad
4. Aakhir mein ek clear **deadline** dena agli demo day ke liye

## Project1 Kya Hai (Recap)
**Problem:** Business ko roz leads aate hain (CSV se), jinhe manually padhna, classify karna, aur urgent waalon ko turant respond karna parta hai.

**Objective:** Python pipeline jo leads ingest kare, AI se classify kare, store kare, aur high-priority leads ke liye email bheje.

## Requirements Checklist (Walkthrough Mein Yeh Padhna Hai)

| # | Requirement | Kis Lecture Se |
|---|---|---|
| 1 | CSV/JSON se leads padhna (ingest) | Lecture09 |
| 2 | Har record validate/clean karna | Lecture09 / Lecture14 |
| 3 | AI se classify karna (structured JSON: category, urgency, reason) | Lecture13 |
| 4 | Result ko output file mein save karna | Lecture09 |
| 5 | High-priority lead ke liye real email notification | Lecture12 |
| 6 | Kam az kam 2 error cases handle karna | Lecture11 / Lecture14 |
| 7 | Ek log file (traceability) | Lecture14 |
| 8 | Secrets `.env` mein, kabhi GitHub pe push nahi | Lecture11 |
| 9 | README jo batae pipeline kaise chalani hai | — |

## Optional / Advanced (Mention Karein, Mandatory Nahi)
- Isi pipeline ka n8n workflow version (Lecture15-16)
- Retry/backoff logic

## Demo Mein Yeh Explain Karna Hoga (Yeh Bhi Aaj Bata Dein)
- Har step Python/API/AI mein kyun kiya
- Errors kaise detect/handle hote hain har stage pe
- AI prompt kaise design kiya taake reliable structured output mile

## Aaj Ke Aakhir Mein
- Deadline confirm karein agli demo day ke liye
- Poochein kisi ko kaunsi requirement samajh nahi aayi
- Yaad dilayein: yeh sab tukde already unke paas hain — sirf jorna aur polish karna hai
