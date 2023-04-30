import random
while(1):
    computer = random.randint(1,3)
    if computer == 1:
        b = 'r'
    elif computer == 2:
        b = 'p'
    elif computer == 3:
        b = 's'
    a = input("Choose Rock(r) Paper(p) or Scissors(s): ")
    if(a == b):
        print("DRAW")
    elif(a == 'r'):
        if(b == 's'):
            print("YOU WIN, CONGRATS PRO !!!")
        else:
            print("YOU LOSE, BETTER LUCK NEXT TIME")
    elif(a == 'p'):
        if(b == 'r'):
            print("YOU WIN, CONGRATS PRO !!!")
        else:
            print("YOU LOSE, BETTER LUCK NEXT TIME")
    elif(a == 's'):
        if(b == 'p'):
            print("YOU WIN, CONGRATS PRO !!!")
        else:
            print("YOU LOSE, BETTER LUCK NEXT TIME")
    print("Do you want to play again? yes(y) no(n)")
    res = input()
    if(res == 'n'):
        break