students={"Ana":[90,85,82],
          "Kirk":[74,76,70]}

students1={"Ana":(90,85,82),
          "Kirk":(74,76,70)}

for name, grade in students.items():
    print(name, *grade)