sub1 = 75
sub2 = 37
sub3 = 91

obt_marks = sub1+sub2+sub3 

total_marks = 300

per = obt_marks / total_marks * 100

grade = ""

# Ladder If Else
if per >= 80: 
    grade = "A+"
elif per < 80 and per >= 70:
    grade = "A"
elif per < 70 and per >= 60:
    grade = "B"
elif per < 60 and per >= 50:
    grade = "C"
elif per < 50 and per >= 40:
    grade = "D"
else:
    grade = "F"

# Interpolation ( F-String )
print(f"Obtained Marks: {obt_marks} \nPercentage: {per} \nGrade: {grade}")

print(type(sub1), type(obt_marks), type(per), type(grade))

# Nested If

rEmail = "hashim@gmail.com"
rPass = "hashim123"
cPass = "hashim123"

logEmail = "hashim@gmail.com"
logPass = "hashim123"

if rPass == cPass: 
    if logEmail == rEmail and logPass == rPass:
        print("Login hogaya yar!")
    else: 
        print("Khuda k bande ghalat hai email or passowrd!")
else: 
    print("Password match nahin hua")


# Input
val = input("Enter your name: ")
print(val)

# Type Casting
# Integer
valOne = int(input("Enter value one: "))
valTwo = int(input("Enter value two: "))
print(valOne + valTwo)

