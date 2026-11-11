# Lecture 15-16 — Workflow Automation with n8n (Intro + Advanced)

Yeh do sessions **no-code** thay — koi Python file nahi, isi liye yeh dono ek hi README mein hain. Kaam n8n ke visual canvas pe (drag-and-drop nodes) hua, VS Code mein nahi.

---

## Din 1 — n8n Intro

### n8n Kyun Ab, Aur Kyun Bilkul
Course ka design principle: pehle Python mein `requests`, JSON, webhooks, AI calls — **sab kuch code se** seekha. Ab wahi cheezein visually, bina code ke dikhayenge. Isi liye n8n Class1 mein nahi, is stage pe aaya — ab pata hai HTTP request, JSON, trigger kya hote hain, is liye n8n sirf ek naya interface lagega, naya concept nahi.

### Core Concepts
- **Node** — ek box jo ek kaam karta hai (Python ke function jaisa)
- **Trigger** — workflow shuru karne wala node (Manual, Schedule, Webhook)
- **Action** — trigger ke baad jo hota hai (HTTP call, transform, notify)
- **Workflow** — nodes ka connected graph; data **JSON** ki shape mein ek node se doosre tak flow karta hai

### Trigger Types
- **Manual** — button dabao, chal jaye
- **Schedule** — har X minute (polling jaisa — Lecture12 ka pizza analogy yaad karein)
- **Webhook** — koi bahar wala system push kare (yehi hai woh inbound webhook jo `webhook.site` pe dekha tha)

### Installation
```bash
npx n8n
```
Free, self-hosted, Docker ki zaroorat nahi. Browser mein `localhost:5678` khulta hai. Pehli dafa ek **local owner account** banana parta hai (sirf local, koi cloud signup nahi).

### Demo Workflow
1. **Manual Trigger** node
2. **HTTP Request** node — URL: `https://jsonplaceholder.typicode.com/users`
3. **Edit Fields (Set)** node — sirf `name`/`email` nikalna
4. "Execute Workflow" se test

Yeh bilkul wahi kaam hai jo Lecture11 mein `requests.get()` se code se kiya tha.

### Assignment (Din 1)
Google Sheet mein sample leads (name, email) banayein, n8n workflow se us Sheet ko padhein, transform karein, doosri Sheet tab mein likhein.

---

## Din 2 — n8n Advanced

### Motivation
Din 1 ki workflow mein koi faisla nahi tha — data seedha chala gaya. Real automation mein hamesha branching chahiye: "agar yeh ho tou yeh karo, warna woh karo."

### IF / Switch Nodes
Bilkul wahi `if/elif` jo Lecture04 mein seekha tha, ab box ki shape mein. `IF` = do raaste (true/false). `Switch` = teen ya zyada raaste (elif chain jaisa).

### Real Apps Connect Karna
- **Google Sheets node** — read/write
- **Gmail node** — Lecture12 ke `notify()` ka no-code version
- **Telegram node** — sirf concept ke tor pe mention (Pakistan mein block, demo mein use nahi kiya)

### Code Node
Jab built-in nodes kaafi na hon, seedha JavaScript/Python likh sakte hain ek node ke andar — code aur no-code ke beech pul.

**AI-Architecture Tie-In:** "Jab no-code kaafi na ho, code likho" — yehi soch hai AI Agent ke **Tools** ki (Class17). Agent bhi jab kuch specific karna ho, ek custom tool (code) call karta hai. Code node aaj wahi role play kar raha hai jo Tool Agent ke liye karega.

### Error Workflows / Fallback Paths
Agar ek node fail ho, poora workflow crash na ho — alag "Error Workflow" trigger ho sakta hai (Lecture11 ke `try/except` ka visual version).

### Decision Framework — Python vs n8n
| Jab Yeh Ho | Use Karo |
|---|---|
| Complex custom logic, deep AI integration | **Python** |
| Multi-app connections, quick setup | **n8n** |
| Dono chahiye | **Hybrid** (n8n + Code node) |

### Demo Workflow
Lecture14 ki Python pipeline (leads.csv → classify → notify) ko n8n mein rebuild: **Sheet Trigger → IF node (urgency == High) → Gmail node (notify) → Sheet node (log)**.

### Assignment (Din 2)
Apni Project1 pipeline (ya simplified version) n8n mein rebuild karayein, kam az kam ek IF node aur ek real app connection ke sath, phir Project1 README mein ek chhota Python-vs-n8n reflection add karayein.

---

## Common Mistakes (Dono Din)
- URL/field names mein typo — node red ho jata hai, error message padhna zaroori hai
- Google account connect na hona — Sheets/Gmail node kaam nahi karega jab tak credential connect na ho
- Bina "Execute Workflow" dabaye yeh soch lena ke workflow chal gaya

## Common Questions
**n8n free hai permanently?**
Haan, self-hosted (`npx n8n`) version free hai — sirf apni machine pe chalti hai, cloud account/paid plan ki zaroorat nahi.

**Kya n8n Python/JavaScript ki jagah le sakta hai?**
Nahi — yeh complement hai, competitor nahi. Complex AI logic Python mein behtar, multi-app quick automation n8n mein behtar.
