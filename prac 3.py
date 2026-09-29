students1 ={"Ana":[90,65,34],
           "Diana":[90,50,69],
            "Ben":[90,78,76]
}
highest = 0
namehighest = ""
tally = 0

for name,grade in students1.items():
    average = sum(grade) / len(grade)
    print(name, *grade, "Average: ", average)
    if average > highest:
        highest = average
        namehighest = name
    for g in grade:
        if g < 75:
            tally = tally + 1

print(f"Student {namehighest} got the highest average: {highest}")
print(f"There are {tally} grades which are below 75")