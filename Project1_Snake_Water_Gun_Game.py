'''Project 1: Snake, Water, Gun, Game or Rock, Paper, Scissor
We all have played snake water gun game in our childhood. If you haven't, google the rules of this game and write a python program capable 
of playing this game with user. '''
import random

def gameWin(comp,you):
        # if two values are equal,declare a tie!
        if comp == you:
            return None
        
        # check for all possibilities when computer chose s
        elif comp == 's':
            if you == 'w':
                return False
            elif you=='g':
                return True
            
        # check for all possibilities when computer chose w
        elif comp == 's':
            if you == 'g':
                return False
            elif you=='s':
                return True
            
        # check for all possibilities when computer chose g
        elif comp == 'g':
            if you == 's':
                return False
            elif you=='w':
                return True
        
        

print("Comp 1 Turn: Snake(s) Water(w) or gun(g)?")
randNo = random.randint(1,3)
print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or gun(g)?")
a = gameWin(comp,you)

print(f"Computer chose {comp}")
print(f"You chose {you}")


if a == None:
    print("The game is a tie! ")
elif a:
    print("You Win!")
else:
    print("You Lose")