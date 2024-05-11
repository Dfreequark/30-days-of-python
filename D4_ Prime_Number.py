# Method 1
def prime():
    number= input("Enter a positive number :")
    number=int(number)
    flag= True
    if number==1:
        flag = False
    elif number==2:
        flag = True
    
    for i in range(2, number):
        if number % i==0:
            flag=False
            print(number, " is divisible by ", i)
            break
        else:
            flag= True

    if flag:
        print(number, " is a prime number.")
    else:
        print(number, " is a not prime number.")

# method 2 
def prime_1():
    number= input("Enter a positive number :")
    number=int(number)
    flag = all((number % i)!=0 for i in range(2, number))
    if flag:
        print(number, " is a prime number.")
    else:
        print(number, " is a not prime number.")

prime()
#prime_1()

