import csv 
import json 
from utils.utils import calculate_percentage, get_status

def process_students(filename): 
    """Yeh csv file read karke student data ko process krega."""
    results = []
    with open(filename, "r") as f: 
        reader = csv.DictReader(f)
        # reader = [ { "name": "Shayan", "obtained": 99, "total": 100 }, { "name": "Ayaan", "obtained": 91, "total": 100 }, { "name": "Aaqib", "obtained": 75, "total": 100 }, { "name": "Hashim", "obtained": 33, "total": 100 }, { "name": "Sufyan", "obtained": 49, "total": 100 } ]
        # print(row["name"])
        for row in reader:
            obtained = int(row["obtained"])
            total = int(row["total"])
            percentage = calculate_percentage(obtained, total)
            row["percentage"] = percentage
            row["status"] = get_status(percentage)
            results.append(row)
    return results

def write_summary(results, filename): 
    """Yeh ek choti summary text file bnata hai jis m Pass/Fail ka count hota hai."""
    pass_count = sum(1 for r in results if r["status"] == "Pass")
    fail_count = len(results) - pass_count
    with open(filename, "w") as f:
        f.write(f"Total Students: {len(results)}\n")
        f.write(f"Pass Students: {pass_count}\n")
        f.write(f"Fail Students: {fail_count}\n")


processed = process_students("files/students.csv")

write_summary(processed, "files/summary.txt")

with open("files/students.json", "w") as f:
    json.dump(processed, f, indent=4)

print(processed)