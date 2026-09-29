print("================PIZZA STORE=================")
soriaFlavor = [("Hawaiian", 250),("Cheese", 300),("Overload", 350)]
soriaSize = [("Small", 0),("Medium", 50), ("Large", 100)]
for n in range(len(soriaFlavor)):
    print(n+1, soriaFlavor[n][0], " - PHP", soriaFlavor[n][1])
print("============================================")
SoriaFlavorSelection = int(input("Please enter the number of the pizza flavor you want to order: "))
print("============================================")
for n in range(len(soriaSize)):
    print(n+1, soriaSize[n][0], "Add PHP", soriaSize[n][1])
print("============================================")
SoriaSizeSelection = int(input("Please enter the number of the size you want to order: "))
SoriaQuantity = int(input("Please Enter the quantity you want to order: "))

SoriaPizzaName = soriaFlavor[SoriaFlavorSelection - 1][0]
SoriaPizzaSize = soriaSize[SoriaSizeSelection - 1][0]
SoriaPizzaPrice = soriaFlavor[SoriaFlavorSelection - 1][1]
SoriaSizeAdd = soriaSize[SoriaSizeSelection - 1][1]

SoriaFinalPrice = (SoriaPizzaPrice + SoriaSizeAdd) * SoriaQuantity

print("===================RECEIPT=================")
print(f"You have selected: ", SoriaPizzaName)
print(f"Size Selected: ", SoriaPizzaSize)
print(f"Total Payment: PHP",SoriaFinalPrice)
print("===========================================")