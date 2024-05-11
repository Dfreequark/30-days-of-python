import random
print("Let's Play A Guessing Game")

answer = int(input("Enter a number between 0,10 \n"))
num = random.randint(0,10)

print(num)
for i in range(2):
    if answer==num:
        print("CONGRADULATIONS: YOU WON")
        break
    else:
        print("Re-enter again.\n You have ", 2-i, " chances left.")
        answer=int(input("Enter here :  "))
    
    



    
