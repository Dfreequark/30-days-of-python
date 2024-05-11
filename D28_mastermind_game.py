'''
Rules of the game
Two players play the game against each other; let’s assume Player 1 and Player 2.

Player 1 plays first by setting a multi-digit number.
Player 2 now tries his first attempt at guessing the number.
If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind! If not, then Player 1 hints by revealing which digits or numbers Player 2 got correct.
The game continues till Player 2 eventually is able to guess the number entirely.
Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind.
If not, then Player 2 wins the game.
output the no of tries each take.

'''

import random

random_no= random.randint(1001,9999)
random_no_list=[ int(digit) for digit in str(random_no)]


def play():
    count=1
    while True:
        guess= input("Guess the 4 digit number or press q to quit : ")
        
        if guess=="q":
            return 
        else:
            guess= int(guess)

        
        guess_list=[int(digit) for digit in str(guess)]
        if guess_list==random_no_list:
            print(f"The number is {random_no}")
            print(f"YOU ARE A MASTERMIND. YOU COMPLETED IN {count} tries.")
            return
        
        correct_list=[]
        correct=0
        for i in range(0,4):
            if random_no_list[i]==guess_list[i]:
                correct_list.append(random_no_list[i])
                correct +=1
            else: 
                correct_list.append("X")

        current_hint= "".join([str(i) for i in correct_list])
        print(f"You have got {correct} correct positions.\n Hint: {current_hint}")
        count +=1

play()

    
    