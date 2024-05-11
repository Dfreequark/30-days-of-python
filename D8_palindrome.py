'''
Problem (Intermediate):
Write a Python function to check if a given string is a palindrome or not. 
(A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.)
'''
"""
algorithm checking:
    1234321
    0123456
    7
    0=7-1 -0
    1=7-1 -1
    2=7-1 -2
    3=7-1 -3
   
"""

#my version
def palindrome(line):
    line =str(line)
    letters=[]
    for char in line:
        if char.isalpha():
            letters.append(char)
        elif char.isdigit():
            letters.append(char)
        else:
            pass


    length=len(letters)
    flag = all(letters[i]==letters[(length-1) -i] for i in range(0,len(letters)//2))
    return flag

#simplest version
def is_palindrome(line):
    line= "".join(char.lower() for char in line if char.isalnum())
    return line==line[::-1]


line = input("enter your string: ").lower()


#flag=palindrome(line)
flag=is_palindrome(line)

if flag:
    print(line, " is a palindrome.")
else:
    print(line, " is not a palindrome.")
  