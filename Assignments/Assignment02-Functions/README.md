# Assignment 02 — Functions

**Based on:** [Lecture 07 — Functions](../../Lectures/Lecture07-Functions)
**Due:** Wednesday, 14 October 2026 (before class)
**Submission:** GitHub par push karke — apna khud ka folder banayein aur usi ke zariye submit karein.

---

## Task 1 — Percentage & Grading System (Function Chaining)

Do functions banayein:

1. **`calculate_percentage(obtained, total)`** — obtained aur total marks lekar percentage calculate kare aur **return** kare.
2. **`get_grade(percentage)`** — percentage lekar uska grade return kare.

`obtained` aur `total` **user se `input()` se** lein.

**Zaroori baat:** Pehle function (`calculate_percentage`) ka output seedha doosre function (`get_grade`) ka argument banna chahiye — yani ek hi call mein obtained/total dete hi percentage bhi nikle aur grade bhi:

```python
grade = get_grade(calculate_percentage(obtained, total))
```

---

## Task 2 — Email Validator (3 Attempts)

Function **`is_valid_email(email)`** banayein jo check kare ke email mein `@` aur `.` dono maujood hain ya nahi.

- User ko email darj karne ke **max 3 attempts** dein.
- Agar koi attempt invalid ho, dobara mauka milega, lekin total 3 se zyada attempts nahi.
- Teen dafa bhi sahi email na aaye tou **"Failed"** print ho aur program ruk jaye.

**Hint:** Yeh wahi retry-pattern hai jo Lecture05 ke login system mein use hua tha (`while` loop + attempts counter).

---

## Task 3 — Number Classifier

Function **`classify_number(num)`** banayein jo number ko **Positive**, **Negative**, ya **Zero** classify kare aur print kare.

---

## Submission Checklist

- [ ] Teeno tasks alag-alag functions mein, docstrings ke sath
- [ ] Task 1 mein function chaining (ek function ka output doosre ka input) sahi se ho
- [ ] Task 2 mein 3-attempts retry logic kaam kar rahi ho
- [ ] Code GitHub repository par push kiya ho
