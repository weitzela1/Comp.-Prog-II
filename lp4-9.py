import random
playernum = int(input("Enter a number between 1 and 20: "))
compnum = random.randint(1,20)
print("Computer's number : " + str(compnum))
print("Players number: " +  str(playernum))


if compnum == playernum:
    print("You won!")

else:
    print("Better luck next time!")