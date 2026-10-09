# Student Info
student = {
    "name": "Shayan", 
    "email": "shayan@gmail.com",
    "course": "Agentic AI", 
    "marks": 90
}


print("---------------- Student Info ----------------")

for key, value in student.items():
    print(f"{key} -> {value}")

user_key = input("Enter new user key (eg.. city, country): ")
user_value = input(f"Enter value for {user_key}: ")

student[user_key] = user_value

print("Final output of student dictonary: ")
for key, value in student.items():
    print(f"{key} -> {value}")