import random
length = random.randrange(8,12)
password = []
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
special = '!@#$%^&*(){.,/;?|}'
digit = '1234567890'
password.append(random.choice(upper))
password.append(random.choice(lower))
password.append(random.choice(special))
password.append(random.choice(digit))
n = 4
while(n <= length):
    x = random.choice(upper+lower+special+digit)
    if x not in password:
        password.append(x)
        n += 1
    
print(''.join(password))
