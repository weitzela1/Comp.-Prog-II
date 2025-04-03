import random

numcount = random.randint(1, 500)
random_nums = [random.randint(1, 1000) for x in range(numcount)]
test = 0
compare = 500
small = []
big = []
for number in random_nums:
    if number < compare:
        small.append(number)
    elif number > compare:
        big.append(number)
    else:
        big.append(number)
print("The amount of numbers less than 500:", (len(small)))
print("The amount of numbers greater than 500:" , (len(big)))
print("The amount of numbers total:", numcount)


