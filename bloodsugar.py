
patients = {"Ana": (80,50,150,90,140,120,60),"Ben": (130,140,135,90,140,150,120),"Carlo":(90,100,95,90,140,190,70)}
high_count = 0
patientName = ""

for patient, readings in patients.items():
    total = 0
    count = 0
    print("\nPatient: ", patient)

    for reading in readings:
        total += reading
        if reading > 120:
            print(reading, " - High")
            count = count + 1
        else:
            print(reading, " - Normal")


    average = total / len(readings)
    diff = max(readings) - min(readings)
    print("Number of High Readings - ", count)
    print("Max reading - ",max(readings))
    print("Min Reading - ", min(readings))
    print(f"Average Reading - {average}")
    print("Difference Reading - ", diff)


    if count > high_count:
        high_count = count
        patientName = patient

print("\nThe patient who had the most high blood sugar count is - ", patientName)

