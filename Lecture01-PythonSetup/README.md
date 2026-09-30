# Lecture 01 — Course Intro, Python Setup & Git/GitHub Basics

## Aaj Ka Overview

Sabse pehle course ka poora vision discuss hua — yeh course sirf "Python seekhna" nahi hai, balke humne baat ki ke yeh course kaise different aur kaam ka hai. Hum real-world projects pe kaam karenge, sirf theory nahi. Poore 2-mahine ke course ke topics pe halki discussion hui taake shuru se hi pata ho ke aage kya kya aane wala hai aur kis tarah har cheez ek dusre pe build hoti hai.

## Python Kya Hai

Python ek programming language hai — humne Python 3 install ki (Python 2 ab use nahi hoti, purani ho chuki hai). Python ki wajah se hi hum data processing se le kar AI Agents tak sab kuch build kar payenge.

## Teen Software Install Kiye

1. **Python** — khud programming language, jisme code chalega
2. **VS Code** — code editor, jahan hum code likhenge
3. **Git** — version control tool, jo humein code ki history track karne aur GitHub pe upload karne dega

## VS Code Setup & Pehli Python File

VS Code mein ek folder khola aur pehli Python file banayi: `lec01-introduction.py`

**`.py` extension kyun?**
Extension file ko batata hai ke andar kaunsi type ka content hai, aur system/editor ko pata chalta hai ke isay kaise chalana hai. `.py` extension Python ko batata hai "yeh ek Python script hai" — isi wajah se VS Code aur Python interpreter dono isay Python code ki tarah treat karte hain.

## Version Control System (VCS) — Concept

Code ki history track karne ke teen tareeqe (types) discuss huye:

1. **Local VCS** — history sirf ek hi computer pe store hoti hai
2. **Centralized VCS** — ek central server pe history store hoti hai, sab log usi se connect hote hain
3. **Distributed VCS** — har banda apne paas poori history ki copy rakhta hai (Git isi type ka hai)

**Git Distributed hai** — is liye har developer ke paas apni local machine pe poora project history ke sath maujood hota hai, sirf ek central server pe depend nahi karna parta.

## Git Kaise Kaam Karta Hai

- Git aapke folder ke andar changes ko "track" karta hai — kaunsi file badli, kya add hua, kya remove hua.
- **GitHub** iske upar ek online platform hai jahan yeh tracked history (repository) upload/host hoti hai, taake code kahin bhi se access ho sake aur duosron ke sath share ho sake.
- Farq yaad rakhein: **Git** = tool jo tracking karta hai (local), **GitHub** = website jahan wo tracking online store hoti hai (remote).

## Git Config — Global Setup

Git ko pehli dafa use karne se pehle apni identity set karni parti hai (taake commits pe pata chale kisne kiya):

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Yeh ek dafa setup hota hai poori machine ke liye (`--global`), har naye repo mein dobara karne ki zaroorat nahi.

## GitHub Account Setup

GitHub pe account banaya — yehi wo jagah hai jahan hamara pura course repo (`AgentCraft`) host hoga, aur har lecture ka code yahin push hoga.

## Git Commands — File Upload Ka Poora Flow

Is tarteeb mein commands chalayi gayin:

1. **`git init`**
   Current folder ko ek Git repository bana deta hai — ab Git yahan tracking shuru kar sakta hai.

2. **`git add .`**
   Saari changed/nayi files ko "staging area" mein le aata hai (commit ke liye ready). `.` ka matlab hai **"sab kuch"** — agar sirf ek specific file add karni ho tou uska naam likh sakte hain, jaise `git add lec01-introduction.py`.

3. **`git commit -m "message"`**
   Staged changes ka ek permanent snapshot bana deta hai history mein, sath ek message ke jo batata hai yeh commit kis liye hai.

4. **`git remote add origin <repository-url>`**
   Local repo ko GitHub wale online repo se link karta hai. **`origin`** sirf ek naam (variable jaisa) hai jo is remote link ko diya jata hai — technically kuch bhi rakh sakte hain, lekin `origin` hi standard best-practice naming convention hai jo har jagah use hoti hai.

5. **`git push origin master`**
   Local commits ko GitHub (remote) pe bhej deta hai, `master` branch pe.

6. **Verification**
   Push karte waqt GitHub identity verify karni parti hai — yeh do tareeqon se ho sakta hai: browser khul kar "Sign in with your browser" se, ya phir ek code/token generate karke terminal mein daal kar.

## Code Walkthrough

`lec01-introduction.py`:

```python
name = "Shayan"
print(name)
```

- `name = "Shayan"` — ek **variable** banaya jiska naam `name` hai aur usme ek **string** value `"Shayan"` store ki.
- `print(name)` — us variable ki value ko terminal/console pe output karta hai.

Yeh sabse pehla working Python program tha — bahut simple, lekin har cheez isi se shuru hoti hai: variable banana aur output dikhana.

## Common Questions / Confusions

**Git aur GitHub mein kya farq hai?**
Git ek tool hai jo aapke computer pe local history track karta hai. GitHub ek website/service hai jahan wo history online store aur share hoti hai. Git ke bina GitHub kaam nahi karega, aur GitHub ke bina bhi Git akele local machine pe chal sakta hai.

**`git add .` mein `.` kyun likhte hain?**
`.` current folder ko represent karta hai — matlab "is folder ki saari changed files add karo." Agar sirf ek file add karni ho tou uska naam directly likh dein.

**`origin` hi kyun likhte hain, koi aur naam kyun nahi?**
`origin` sirf ek naming convention hai — Git ko koi farq nahi parta aap kya naam rakhte hain, lekin poori duniya mein `origin` hi standard practice hai, is liye hum bhi wahi follow karte hain taake code readable/consistent rahe.

**Distributed VCS ka fayda kya hai Centralized ke muqable mein?**
Distributed mein har developer ke paas poori history apne paas hoti hai — agar central server (GitHub) down bhi ho jaye, tab bhi aap apni local machine pe kaam kar sakte hain, aur baad mein sync kar sakte hain.

## Is Lecture Ko Kaise Run Karein

1. `Lecture01-PythonSetup` folder VS Code mein open karein.
2. Terminal mein likhein:
   ```bash
   python lec01-introduction.py
   ```
3. Output mein `Shayan` print hoga.
