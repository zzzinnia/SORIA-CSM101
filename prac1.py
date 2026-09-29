students = {
    "Ana": 85,
    "Ben": 98,
    "Carlo": 78,
    "Diana": 95
}
print("STUDENT GRADES")
print("---------------")
print("Ana: ", students["Ana"])
print("Ben: ", students["Ben"])
print("Carlo: ", students["Carlo"])
print("Diana: ", students["Diana"])
name1 = input("Enter a students name: ")
grade1 = int(input("Enter the students grade: "))
students[name1] = grade1
print(name1,": ", students[name1])
for name, grade in students.items():
    print(name, grade)
search = input("Enter the name of the student you want to search: ")
found = False
for name, grade in students.items():
    if search.lower() == name.lower():
        print(name,"Grade is: ", grade)
        found = True
        break
    else:
        continue
if not found:
    print("Student not found")
