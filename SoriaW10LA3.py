while True:
    SoriaPass = input("Please Enter a Strong Password (REQUIRED TO HAVE A CAPITAL AND A NUMBER): ")

    SoriaCaps = False
    SoriaNum = False

    for character in SoriaPass:
        if character.isdigit():
            SoriaNum = True

        if character.isupper():
            SoriaCaps = True


    if SoriaCaps == True and SoriaNum == True:
        print("You have entered a Good Password")
    elif SoriaCaps == True and SoriaNum != True:
        print("Please enter number to your password")
    elif SoriaCaps != True and SoriaNum == True:
        print("Please enter a Capital Letter to your Password")
    else:
        print("Password does not meet any of the requirements")

    c = input("Do you want to continue? (Y/N): ")

    if c.upper() != "Y":
        print("Program Ending")
        break