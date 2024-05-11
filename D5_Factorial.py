def factorial():
    while True:
        number =input("Enter a number : ")
        if number.isdigit():
            number=int(number)
            if number>=0:
                break
            else:
                print("Enter a non-negative interger.")
        else:
            print("Enter a number in digits.")
    value= 1
    for i in range(1,number+1):
        value = value*i

    print(f"{number}!={value}")
#factorial()



# using recursive function
def factorial_val(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: return n times the factorial of (n-1)
    else:
        return n * factorial_val(n-1)

# Test the function
print(factorial_val(5))  # Output: 120 (5! = 5*4*3*2*1)
print(factorial_val(0))  # Output: 1 (0! = 1)
print(factorial_val(1))  # Output: 1 (1! = 1)

