# Lecture 02 — Data, Data Types, Variables & Operators

## Aaj Kya Parha

Aaj hum ne programming ki sabse buniyaadi cheez se shuruat ki — **Data**. Har program aakhir mein data ko store, process, aur compare karta hai. Is lecture mein humne dekha ke data ko uske **format** ke hisaab se different types mein baanta jata hai, phir usay variables mein store karna seekha, aur phir un values pe operations (operators) chalana seekha.

## Data Kya Hoti Hai

Data koi bhi value hoti hai jo hum store ya use karna chahte hain — jaise ek naam, ek number, ya ek true/false decision. Har value ki apni ek **format** hoti hai, aur usi format ke hisaab se uski ek limit ya length hoti hai (jaise ek number ki value kitni bari ho sakti hai, ya ek text kitna lamba ho sakta hai).

## Data Types (Format Ke Basis Par)

Python mein data types isi liye bante hain ke value **kis format mein** likhi gayi hai. Aaj humne yeh 4 types cover kiye:

| Type | Format / Rule | Example |
|---|---|---|
| **String (`str`)** | Har wo value jo **inverted commas** (`" "` ya `' '`) mein ho | `"Shayan"` |
| **Integer (`int`)** | Har wo number jis par calculation ho sake, **decimal point na ho** | `18` |
| **Float (`float`)** | Har wo number jis par calculation ho sake **aur decimal point bhi accept kare** | `3.7` |
| **Boolean (`bool`)** | Sirf do possible values — `True` ya `False` | `True` |

## Variables

Ek **variable** ek storing container hota hai — jismein hum koi bhi data value rakh sakte hain taake usay baad mein use kar sakein.

```python
name = "Shayan"   # yahan 'name' ek variable hai jo string store kar raha hai
```

`=` yahan **Assignment Operator** hai — iska matlab hai "right side ki value ko left side wale variable mein rakh do." (Yeh comparison wale `==` se bilkul alag hai — neeche Common Mistakes mein detail hai.)

### Naming Conventions
Variable ka naam likhne ka standard style **camelCase** hai:
- Pehla word chhota (lowercase) — `isVerified`
- Agla word capital se shuru — `isVerified`, `myTwoWords`
- Spaces allowed nahi, is liye words ko jorne ke liye yeh style use hoti hai.

## Keywords

Keywords Python ki wo **reserved words** hain jo language ka hissa hain — inhe variable ka naam nahi rakh sakte (jaise `if`, `else`, `True`, `False`, `and`, `or`, `not`). Python inhe already apne kaam ke liye reserve kar chuki hai.

## Operators

### Assignment Operator
`=` — value ko variable mein store karta hai.

### Arithmetic Operators
`+` `-` `*` `/` — addition, subtraction, multiplication, division.

**Remainder Operator (`%`)** — do numbers ki division ka **baqiya (leftover)** deta hai. Aaj ka sabse important use case yeh tha:
```python
year % 4 == 0   # agar 0 bache tou year 4 se pura divide ho raha hai
```

### Comparison Operators
`==` (barabar hai?), `!=` (barabar nahi?), `>`, `<` — yeh hamesha **`True`/`False` (bool)** return karte hain.

### Logical Operators
- `and` → dono conditions True hon tabhi True
- `or` → koi bhi ek condition True ho tou True
- `not` (`!`) → result ko ulta (reverse) kar deta hai — `not True` → `False`

## String Concatenation (Comma Se)

Aaj hum ne `print()` ke andar **comma (`,`)** se multiple values ko jodh kar print kiya:
```python
print("Name:", name)   # comma khud-ba-khud beech mein ek space add kar deta hai
```
**Note:** Yeh **concatenation** ka simple tareeqa hai. **Interpolation** (f-strings, jaise `f"Name: {name}"`) agli lecture mein cover hogi — abhi sirf comma wala style use karein.

## Conditionals — `if` / `else` (Intro)

Aaj sirf `if` / `else` ka basic structure introduce hua hai (`elif` abhi nahi):
```python
if (year % 4 == 0):
    print("Leap Year")
else:
    print("Not a leap year")
```

**C++ se farq (jo class mein discuss hua):** Python mein block ko `{ }` se nahi, **colon (`:`) aur indentation** se define karte hain, aur line ke aakhir mein `;` ki zaroorat nahi hoti.

## Syntax Guide

| Concept | C++ Style | Python Style |
|---|---|---|
| Block shuru/khatam | `{ }` | `:` + indentation |
| Line ka end | `;` | Kuch nahi (sirf nayi line) |
| Comment | `//` | `#` |
| Condition | `if (x > 5) { }` | `if x > 5:` |
| Assign vs Compare | `=` assign, `==` compare | Same rule: `=` assign, `==` compare |

## Common Mistakes

- **`=` aur `==` mix karna** — `=` value store karta hai, `==` compare karta hai. `if score = 80` likhna error dega, sahi hai `if score == 80`.
- **String ko inverted commas ke bina likhna** — `name = Shayan` error dega; sahi `name = "Shayan"`.
- **Integer mein decimal daal dena** — `age = 18.0` likhne se woh `int` nahi rahega, `float` ban jayega. Agar `int` chahiye tou decimal na likhein.
- **Indentation ka khayal na rakhna** — Python mein `if`/`else` ke andar ka code sahi indent (spaces) mein hona zaroori hai, warna `IndentationError` aayega.
- **camelCase mein inconsistent naming** — kabhi `my_word` kabhi `MyWord` likhna — ek hi convention pe consistent rahein.

## Common Questions / Confusions

**C++ mein `char` hota hai jo sirf ek word/character accept karta hai — Python mein `char` kahan hai?**
Python mein alag se `char` type nahi hoti. Ek single character bhi Python mein sirf ek **`str`** hi hota hai (jiski length 1 ho) — `"A"` aur `"Hello"` dono `str` hain, Python inhe alag treat nahi karta.

**C++ mein `float` aur `double` alag hote hain — Python mein `double` kahan hai?**
Python mein sirf **`float`** hota hai, aur woh internally wahi precision deta hai jo C++ ka `double` deta hai (64-bit). Python ko alag se `double` type ki zaroorat nahi parti — `float` hi kaafi hai.

**`and`/`or` aur `&&`/`||` (jo C++ mein hote hain) mein farq?**
Python English words use karta hai — `and`, `or`, `not` — jabke C++ symbols use karta hai. Kaam wahi hai, sirf likhne ka tareeqa alag hai.

## Code Walkthrough (`main.py`)

1. **Variables & Data Types** — `name` (str), `age` (int), `gpa` (float), `isVerified` (bool) banaye aur `type` samajhne ke liye print kiye.
2. **Arithmetic Operators** — `score1`, `score2` pe addition, subtraction, multiplication, division dikhaye.
3. **Comparison Operators** — `==`, `>`, `<` se `score1` aur `score2` compare kiye — result hamesha `True`/`False`.
4. **Remainder + Conditional** — `year % 4 == 0` se leap year check kiya (yeh simplified version hai — real leap year rule mein century wala extra condition bhi hota hai, jo aage discuss hoga).
5. **Even/Odd Check** — `num % 2 == 0` se even/odd check kiya (`0` ka case abhi ignore kiya gaya hai kyunke `elif` abhi nahi padhaya).

## Is Lecture Ko Kaise Run Karein

```bash
python main.py
```
