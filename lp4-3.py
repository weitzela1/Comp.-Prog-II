eggs = int(input("Please enter the amount of eggs for purchase: "))
price = 0.0

if 0 < eggs <= 47:
    price = .50/12
elif 47 < eggs <= 71:
    price = .45/12
elif 71 < eggs <= 131:
    price = .40/12
elif eggs >= 132:
    price = .35/12
else:
    print("Invalid # of eggs!")
    quit()

print("The price per egg is $" + str(round(price, 2)))
print("The total cost is $" + str(round(price * eggs, 2)))