import random
print("WELCOME TO GUESS THE NUMBER !!!")
print()
print()
print("Enter the range of the number: ")
lower,upper = input().split()
lower = int(lower)
upper = int(upper)
num = random.randrange(lower,upper)
print("Enter the number of attempts you wish to have - ")
attempts = int(input())
flag = False
while(attempts):
    print(f"Enter your guess between {lower} and {upper}")
    n = int(input())
    if(n==num):
        print("That's the right guess, YOU WIN !!")
        flag = True
        break
    elif(n>num):
        print("Too high !")
    else:
        print("Too low")
    attempts -= 1
    print(f"You have {attempts} attempts remaining.")
else:
    print(f"You LOSE, the correct number was {num}")

