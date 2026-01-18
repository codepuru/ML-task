#guess number
#Purushrut Chauhan 25BEC080
import random
p = random.randint(1 , 50)
print('WELCOME to Guess a Random Number BETWEEN 1 and 50')
print('ONLY 3 CHANCES')

chance = 3
while chance>0:
    guess=int(input('Select a number : \n'))    
    if guess>50 or guess<0:
        print('Number is out of range')
        break
    if guess==p:
        print('That is the correct choice')
        break
    else:
        print('Try Again !!')
        chance -= 1
        print(chance , 'Chances left')
print('GAME OVER !!!')        
        
print(p, 'is the correct answer')
