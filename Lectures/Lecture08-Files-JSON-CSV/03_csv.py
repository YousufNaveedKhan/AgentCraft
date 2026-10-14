import csv 

with open("files/student.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "email"])
    writer.writerow(["Aaqib", 22, "aaqib@gmail.com"])
    writer.writerow(["Shayan", 21, "shayan@gmail.com"])

with open("files/student.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader: 
        print(row)
