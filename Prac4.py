myDic = {}
number = int(input("Please input the number of students"))

for i in range(number):
    print("\nStudent: ", i + 1)

    name = input("Enter students name: ")

    grade1 = float(input("Enter first grade: "))
    grade2 = float(input("Enter second grade: "))
    grade3 = float(input("Enter third grade: "))

    myDic[name] = (grade1,grade2,grade3)

for name, grade in myDic.items():
    print(f"{name}'s Grade is: ", *grade)
