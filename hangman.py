import random
def nope():
    print('  +---+')
    print('      |')
def oneinc():
    print('  +---+')
    print('  o   |')
    print()
    print()
def twoinc():
    print('  +---+')
    print('  o   |')
    print(' /    |')
    print()
    print()
def threeinc():
    print('  +---+')
    print('  o   |')
    print(' /|   |')
    print()
    print()
def fourinc():
    print('  +---+')
    print('  o   |')
    print(' /|\  |')
    print()
    print()
def fiveinc():
    print('  +---+')
    print('  o   |')
    print(' /|\  |')
    print('/     |')
    print()
    print()
def sixinc():
    print('  +---+')
    print('  o   |')
    print(' /|\  |')
    print(' / \  |')
    print()
    print()

ls = ['moon', 'sun' , 'plants', 'joker', 'match', 'query', 'prince' , 'king', 'modern', 'swing', 'corn', 'cats', 'mouse']
word = random.choice(ls)
appearing_letters = random.choice(word)
missed = ''
hang = 0
for j in word:
    if j in appearing_letters:
        print(j,end='')
    else:
        print('_',end='')
print()
print()
while(len(missed) <= 10):
    print("Please give a letter. ")
    letter = input()
    if letter in word:
        if hang == 0:
            nope()
        if hang == 1:
            oneinc()
        elif hang == 2:
            twoinc()
        elif hang == 3:
            threeinc()
        elif hang == 4:
            fourinc()
        elif hang == 5:
            fiveinc()
        elif hang == 6:
            sixinc()
        print("Cheers! You got that correct")
        print()
        if letter not in appearing_letters:
            appearing_letters = appearing_letters + letter
        for j in word:
            
            if j in appearing_letters:
                print(j,end='')
            else:
                print('_',end='')
        print('\n')
        print(f'Missed Words: {missed}')
        print()
        if(len(appearing_letters) == len(word)):
            print("Hurray! You got all of them correct...")
    else:
        hang += 1
        if hang == 1:
            oneinc()
        elif hang == 2:
            twoinc()
        elif hang == 3:
            threeinc()
        elif hang == 4:
            fourinc()
        elif hang == 5:
            fiveinc()
        elif hang == 6:
            sixinc()
        print("Sorry this letter doesnt exist in the word.! ")
        missed = missed + letter + ' '
        for j in word:
            if j in appearing_letters:
                print(j,end='')
            else:
                print('_',end='')
        print('\n')
        print(f'Missed Words: {missed}')
    if(len(appearing_letters) == len(word)):
        break
else:
    k = len(appearing_letters)
    print('You have run out of guesses!')
    print(f'After 6 missed guesses and {k-1} correct guesses, the word was "{word}"')




