import json 

student = {"name": "Shayan", "age": 22, "email": "shayan@gmail.com"}

# json dump => Meri file likho!
with open("files/studentTwo.json", "w") as f:
    json.dump(student, f, indent=4)

with open("files/studentTwo.json", "r") as f:
    data = json.load(f)
