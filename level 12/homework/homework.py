guess = int(input("guess the dice roll: "))

dice_roll = 5

if guess != dice_roll:
    print("thats a wrong number")
elif guess > 6:
    print("thats bigger than number range")
else:
    print("thats correct")



