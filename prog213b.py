num = int(input("Enter Quantity: "))
price = 0
if num < 100:
    price = 5.95
elif num > 99 and num < 200:
    price = 5.75
elif num > 199 and num < 300:
    price = 5.40
elif num > 299:
    price = 5.15
total = price * num
print("Price:", price)
print("Amount due:",total)
