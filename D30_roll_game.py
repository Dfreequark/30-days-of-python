import random

def roll():
    return random.randint(1,6)

print("***  WELCOME TO THE ROLL GAME  *** ")

num= int(input("\n How many players are playing?"))
player_list=[]
for i in range(num):
    name=input("Enter player's name :").upper()
    player_list.append(name)

print(" WELCOME EVERYONE. LET's PLAY THE GAME ")


grand_score= [0]*num

while True:
    opt= input("Press q to quit").lower()
    if opt=="q":
        break
    

    for i in range(2):
        print("\n", player_list[i], "'s TURN")
        score=[0]*num

        while True:
            
            inp= input("\n PRESS R to roll/ S to stop  or q to QUIT (R/S/q):").lower()
            if inp=="q":
                break
            
            elif inp =="r":
                dice_no = roll()

                if dice_no == 1:
                    print("\n Oh You GOT 1. Time to stop rolling")
                    break
                else:
                    score[i] = score[i] + dice_no
                    print("\n You got ", dice_no, ". Total Score :", score[i])
            
            elif inp=="s":
                grand_score[i] = grand_score[i] + score[i]
                break
            else:
                continue
        if grand_score[i] >=50:
            print("CONGRADULATIONS ", player_list[i], ". YOU WON")
        
        print("Grand score of ", player_list[i], " is :", grand_score[i])
        


