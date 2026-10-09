# List
students = ["Aaqib", "Hashim", "Shayan", "Sufyan"]
print(students)
print(students[2])

name = "Ayaan"
students.append(name)
print(students)

students.remove(name)
print(students)

print("Length of Students List: ", len(students))

for student in students: 
    print(student)

# Dictionary
student = {
    "name": "Aaqib", 
    "age": 20, 
    "email": "aaqib@gmail.com", 
    "course": "Agentic AI"
}

print(student)
print("Course: ", student["course"])
print(student.keys())
print(student.values())
print(student.items())

student["grade"] = "A"

for key, value in student.items():
    print(f"{key} - {value}")


users = [
    { "name": "Aaqib", "age": 20, "email": "aaqib@gmail.com", "city": "Karachi" },
    { "name": "Shayan", "age": 18, "email": "shayan@gmail.com", "city": "Peshawar" },
    { "name": "Sufyan", "age": 14, "email": "sufyan@gmail.com", "city": "Islamabad" },
    { "name": "Hashim", "age": 17, "email": "hasim@gmail.com", "city": "Karachi" }
]

print(users)


for user in users: 
    for key, value in user.items():
        print(f"{key} -> {value}")
