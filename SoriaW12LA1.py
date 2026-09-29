classrecord = {
    "Liza": {"StudID": "5001", "Grade": [90, 85, 80, 82, 83, 90, 92]},
    "Jeremy": {"StudID": "5002", "Grade": [90, 75, 64, 80, 84, 75, 85]},
    "Maria": {"StudID": "5003", "Grade": [88, 91, 79, 85, 90, 84, 87]},
    "John": {"StudID": "5004", "Grade": [55, 62, 70, 58, 65, 72, 60]},
    "Anna": {"StudID": "5005", "Grade": [95, 92, 98, 96, 94, 99, 97]},
    "Carlos": {"StudID": "5006", "Grade": [78, 82, 80, 75, 79, 81, 83]},
    "Bea": {"StudID": "5007", "Grade": [92, 88, 90, 85, 89, 91, 87]},
    "Kevin": {"StudID": "5008", "Grade": [45, 58, 62, 50, 55, 60, 53]},
    "Sofia": {"StudID": "5009", "Grade": [85, 89, 84, 88, 90, 86, 91]},
    "David": {"StudID": "5010", "Grade": [70, 72, 68, 75, 74, 71, 76]}
}

userSearch = input("Enter Student Name or ID: ").lower()

found = False

for name, records in classrecord.items():
    if userSearch == name.lower() or records["StudID"] == userSearch:
        print("Student Found!")
        print("Name: ", name)
        print("ID Number: ", records["StudID"])
        print("Grades: ", records["Grade"])
        average = sum(records["Grade"]) / len(records["Grade"])
        print(f"Average Grade: {average:.2f}")
        print("Max Grade: ", max(records["Grade"]))
        print("Min Grade: ", min(records["Grade"]))
        found = True
        for grade in records["Grade"]:
            if grade < 60:
                print("Candidate for intervention")
                break

if not found:
    print("Student not found")
