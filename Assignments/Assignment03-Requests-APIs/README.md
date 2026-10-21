# Assignment 03 — Working with APIs (`requests`)

**Based on:** [Lecture 11 — Requests Library & API Auth](../../Lectures/Lecture11-RequestsLibrary-APIAuth)
**Due:** Friday, 23 October 2026 (before class)
**Submission:** GitHub par push karke — apna khud ka folder banayein aur usi ke zariye submit karein.

---

## Task 1 — GET Request + Query Parameter

Kisi bhi free public API (jaisa `jsonplaceholder.typicode.com`, ya koi aur jo aap khud dhoondein) se ek `GET` request banayein.

- Response ka `status_code` aur JSON data dono print karayein.
- Isi call mein **kam az kam ek query parameter** use karayein (`params={...}`).

---

## Task 2 — POST Request

Ek `POST` request banayein jo apni marzi ka data (ek dictionary, `json=` ke zariye) server ko bheje, aur response print kare.

---

## Task 3 — Secrets via `.env`

Apni khud ki `.env` file banayein jisme ek dummy `API_KEY` rakhein. `python-dotenv` se usay load karein aur print karayein — taake practice ho jaye ke secrets kabhi seedha code mein nahi likhni.

---

## Task 4 — Error Handling

Kam az kam ek jagah **jaan-boojh kar ek ghalat URL** call karayein, aur `try`/`except` se usay gracefully handle karayein (crash na ho, bajaye iske ek samajh aane wala message print ho).

---

## Submission Checklist

- [ ] Query parameter sahi se use hua ho
- [ ] POST request kaam kar rahi ho
- [ ] `.env` + `python-dotenv` sahi tareeqe se use hua ho (`.env` GitHub par push nahi honi chahiye — `.gitignore` check kar lein)
- [ ] Ek failed request `try`/`except` se handle ho
- [ ] Code GitHub repository par push kiya ho
