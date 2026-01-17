
#guess number
#Purushrut Chauhan 25BEC080


import random
p = random.randint(0 , 50)
print('WELCOME to Guess a Random Number BETWEEN 1 and 50')
print('ONLY 3 CHANCES')
chance = 3
while chance>0:
    guess=input('Select a number : \n')
    if guess==p:
        print('That is the correct choice')
        break
    else:
        print('Try Again !!')
        chance -= 1
        print(chance , 'Chances left')
        
print('GAME OVER !!!') 
print(p, 'is the Correct Answer')
        

