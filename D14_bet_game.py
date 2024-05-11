import random as rd


def BET_GAME():

    def deposit():
        
        while True:
        
            deposit_amount= input("Enter the amount you want to deposit, $")
            if deposit_amount.isdigit():
                deposit_amount= int(deposit_amount)
                if deposit_amount<10:
                    print("Deposit has to greater than $10")
                else:
                    print("You succesfully deposited $",deposit_amount)
                    return deposit_amount
            else:
                print("Enter amount in digits")

    def random_number():
        rd_no = rd.randint(1,10)
        return rd_no

    def bet_no():
        while True:
            guess_input = input("Enter the player number you want to bet :")

            if guess_input.isdigit():
                guess_input= int(guess_input)
                if 1<=guess_input<=10:
                    print("You betted on player no ", guess_input)
                    return guess_input
                else:
                    print("SELECT THE PLAYER FROM 1 to 10, (1-10)")
                    
            else:
                print("Enter player no in digits 1 to 10")

    def bet_amount():
        while True:
            bet_amount= input("Enter the amount you want to bet, $")
            if bet_amount.isdigit():
                bet_amount= int(bet_amount)
                if 0<bet_amount<balance: 
                    print("You betted  $", bet_amount)
                    return bet_amount
                else:
                    print("Your balance is $", balance, ". You don't have sufficient balance.")
                    
            else:
                print("Enter bet amount in digits")



    def game():
        player_won= random_number()
        guess= bet_no()
        amount=bet_amount()
        current = 0
        
        if player_won==guess:
            current += 2*amount
            print("Congrates. Player no ", player_won, " won. You have won $", 2*amount)
            return current
        else:
            current -= amount
            print("Player no ",player_won, " won the game. You lost $", amount )
            return current




    def play_again(balance):
        while True:
            ply_agn_inp=input("To play again PRESS Y, to stop PRESS N (Y/N) : ").lower()
            
            if ply_agn_inp=="n":
                print("Thank you for playing. Your balance is $", balance)
                break
            elif ply_agn_inp=="y":

                while True:
                    deposit_amount_new= input("Enter the amount you want to deposit (else enter 0) $")
                    if deposit_amount_new.isdigit():
                        
                        deposit_amount_new= int(deposit_amount_new)
                        balance += deposit_amount_new
                        print("You succesfully deposited $",deposit_amount_new)
                        print("Your current balance is $", balance)
                        
                        

                        balance += game()       
                        print("  Your balance is $", balance)

                        break
                    else:
                        print("Enter valid input")
                break
            else:
                print("Enter a valid input")
                pass
        return balance
            

    #for 1st round
    balance=0
    balance += deposit()
    balance +=game()
    print("  Your balance $", balance)


    while True:   

        balance= play_again(balance)
        
        ply_agn_inp=input("PRESS q to quit : ").lower()
        if ply_agn_inp=="q":
            break

        
