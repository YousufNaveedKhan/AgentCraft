# Assignment 01 — Data Types, Operators & Conditionals

**Based on:** [Lecture 02 — Data, Data Types, Variables & Operators](../../Lectures/Lecture02-FoundationalTopics/README.md)
**Due:** Friday, 2 October 2026 (before next class)
**Submission:** GitHub par push karke — is repository mein apna khud ka folder banayein aur usi ke zariye submit karein.

## Important Rule

Sirf woh cheezen use karein jo ab tak class mein padhi ja chuki hain: variables, data types, arithmetic/comparison/logical operators, aur sirf **`if` / `else`** (abhi **`elif`** use nahi karna — woh agli lecture mein aayega).

---

## Task 1 — Mark Sheet (Percentage & Pass/Fail)

5 subjects ke marks **hardcode** karein (variables mein directly likh dein, `input()` ki zaroorat nahi):

1. Har subject ke marks ek variable mein rakhein (5 variables).
2. **Obtained marks** — sab subjects ke marks jama karein (total).
3. **Percentage** nikalein — `(obtained marks / total marks) * 100`.
4. Percentage ko check karein: agar ek fix passing percentage (jaise 40%) se zyada ya barabar hai tou **"Pass"** print karein, warna **"Fail"**.

**Hint:** Yeh sirf ek `if` / `else` se ho jayega — `elif` ki zaroorat nahi.

---

## Task 2 — Leap Year Checker (Birth Year Se)

Apna birth year ek variable mein hardcode karein, aur check karein ke woh leap year hai ya nahi — Lecture 02 mein jo `year % 4 == 0` wala logic dikhaya gaya tha, wahi use karein.

---

## Task 3 — Even / Odd Checker

Koi bhi number hardcode karein aur `%` (remainder operator) se check karein ke woh **even** hai ya **odd**.

**Note:** `0` ka case abhi ignore kar dein (usay filhal even ya odd kuch bhi maan lein) — kyunke uska sahi handling `elif` se hoti hai, jo abhi nahi padhaya gaya.

