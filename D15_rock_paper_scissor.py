import random

you_win=0
comp_win=0
draw = 0
options=["rock", "paper", "scissors"]

while True:
    your_move = input("Choose Rock/Paper/Scissors or q to quit : ").lower()

    if your_move =="q":
        break


    if your_move not in options:
        continue

    random_number = random.randint(0,2)
    comp_move= options[random_number]

    print("Your Move : ", your_move)
    print("Computer Move : ", comp_move)

    if your_move=="rock" and comp_move=="scissors":
        print("YOU WON")
        you_win +=1
    elif your_move=="paper" and comp_move=="rock":
        print("YOU WON")
        you_win +=1
    elif your_move=="scissors" and comp_move=="paper":
        print("YOU WON")
        you_win +=1    
    elif your_move == comp_move:
        print("It's a Draw")
        draw +=1
    else:
        print("YOU LOST")
        comp_win +=1
print("------------------------------------------")
print("|YOUR SCORE                      |", you_win, "|")
print("-----------------------------------------------")

print("|COMPUTER SCORE                  | ", comp_win, "|")
print("-----------------------------------------------")

print("|Draw                            |", draw, "|")
print("-----------------------------------------------")

