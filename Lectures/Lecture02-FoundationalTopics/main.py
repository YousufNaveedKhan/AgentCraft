# --------- 1. Variables & Data Types ---------
name = "Shayan" # str
print("Name:", name) 

age = 18 # int
print("Age:", age)

gpa = 3.7 # float
print("GPA:", gpa)

isVerified = True # bool
print("Verfied:", isVerified)

# --------- 2. Operators ---------
score1 = 45
score2 = 81

print("Addition:", score1 + score2) # Arithmetic / Addition
print("Substract:", score2 - score1) # Arithmetic / Substract
print("Multiply:", score1 * score2) # Arithmetic / Multiply
print("Divide:", score1 / score2) # Arithmetic / Divide
print("Score 1 is equal to score 2:", score1 == score2) # Logical / Compare
print("Score1 is greater than score 2:", score1 > score2) # Logical / Greater than
print("Score1 is less than score 2:", score1 < score2) # Logical / Less than

# Remainder ( % )
year = 2010

if (year % 4 == 0):
    print("Leap Year")
else:
    print("Not a leap year")

num = 0

if (num % 2 == 0):
    print("Even")
else: 
    print("Odd")