# Lecture 10 — Understanding APIs & Postman

## Aaj Kya Parha

Aaj koi Python code nahi likha — yeh ek **concept + exploration** wala din tha. Ab tak humara data file se ya hardcoded tha; aaj humne seekha ke Python kaise kisi **doosre system se live data** mangwa sakta hai — aur yeh sab Postman mein, bina ek line code likhe, test kaise karte hain.

## Client-Server Model & REST

Jab do systems ek dusre se baat karte hain (jaise aapka phone aur Instagram ka server), unke beech ek **tareeqa (protocol)** hota hai baat karne ka — isay **REST API** kehte hain.

**Restaurant Waiter Analogy:**
- **Aap (Client)** menu dekh kar order dete hain
- **Waiter (API)** order kitchen tak le jata hai
- **Kitchen (Server)** khana bana kar deta hai

Aapko kitchen ke andar ki detail janne ki zaroorat nahi — bas waiter (API) se sahi tareeqe se maangna hai. Jahan data milta hai (jaise `/users`), usay **Endpoint** kehte hain.

## HTTP Methods

| Method | Kaam |
|---|---|
| **GET** | Data mangna (jaise menu dekhna) |
| **POST** | Naya data bhejna (jaise order dena) |
| **PUT** | Existing data update karna |
| **DELETE** | Data hatana |

## Status Codes

| Code | Matlab |
|---|---|
| `200` | Sab theek (OK) |
| `400` | Aap ne galat request bheji (Bad Request) |
| `401` | Aap authorized nahi hain |
| `404` | Jo mangwa rahe hain woh exist nahi karta (Not Found) |
| `500` | Server ki apni ghalati |

## Request Ki Anatomy — Headers, Params, Body

- **Query Parameters** — URL ke `?` ke baad wali values, jaise `?city=Karachi`
- **Path Parameters** — URL ke andar hi ek id, jaise `/users/5`
- **Request Body** — POST/PUT ke sath bheja jane wala data (JSON format mein)
- **Headers** — extra info jo request ke sath jati hai (jaise authentication token)

## Postman Demo

Do free, no-signup APIs test ki:

1. **`GET https://jsonplaceholder.typicode.com/users`**
   Response mein ek list of objects aayi — stress yeh hua ke **yeh exact wahi "list of dictionaries" shape hai jo Lecture06 mein Python mein seekhi thi.** API se data aata hi isi shape mein hai.

2. **`GET https://restcountries.com/v3.1/name/pakistan`**
   Ek thora nested JSON dekha (ek object ke andar aur objects/lists).

Postman mein dikhaya: URL likhna → Method select karna (GET) → "Send" dabana → neeche Response tab mein JSON aur status code (`200`) dekhna.

## Common Mistakes

- **Method ghalat select karna** — `GET` ki jagah `POST` select kar lena, phir confuse hona ke response kyun nahi aa raha.
- **URL mein typo** — ek chhoti spelling mistake se `404 Not Found` aa jata hai.
- **Status code ko ignore karna** — response dekhne se pehle hamesha status code check karein; `200` nahi hai tou data bhi shayad sahi nahi hai.

## Common Questions / Confusions

**API aur Website mein farq kya hai?**
Website insaan ke dekhne ke liye hoti hai (HTML/design). API sirf **data** deti hai (JSON format mein) — koi design nahi, sirf raw information jo koi program use kar sake.

**Postman se directly data mil raha hai, tou Python ki zaroorat kyun?**
Postman sirf **test/explore** karne ke liye hai — manually, ek dafa. Real automation mein hum chahte hain ke Python **khud-ba-khud, repeatedly, bina insaan ke** yeh calls kare. Agli lecture mein yehi seekhenge (`requests` library).

**Har API free hoti hai?**
Nahi — kuch APIs free hoti hain (jaise aaj wali demo), kuch ke liye account/API key chahiye hoti hai. Jab hum Gemini AI API tak pahunchenge, wahan bhi ek free-tier key lagegi.

## Is Lecture Mein Koi Code Nahi — Postman Khud Try Karein

1. [Postman](https://www.postman.com/downloads/) install karein (ya web version use karein).
2. Naya request banayein, method `GET` select karein.
3. URL mein `https://jsonplaceholder.typicode.com/users` likhein.
4. **Send** dabayein, aur neeche Response mein JSON dekhein.

## Aage Kya Aayega (Next Lecture)

- Python ki `requests` library se yeh sab calls code se karna
- `.env` se API keys secure rakhna
- Lecture09 ke data ko live API se enrich karna
