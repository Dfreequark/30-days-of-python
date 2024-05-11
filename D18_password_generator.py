'''
Password Generator
parameters:
Length,Character Set, Complexity(requiring a minimum number of characters from each character set)
Avoidance of Ambiguous Characters(such as 'l', '1', 'I', '0', and 'O')
Avoidance of Common Substrings(such as consecutive characters or repeated sequences)

Note: 1. mix upper- and lower-case letters
2.add numbers or other keyboard characters
3.How many of each character should be included? 
'''
import random

def generate_password():
    length=9
    mode= input("SELECT DIFFICULTY LEVEL: Easy(E), moderate(M), strong(S) :(E/M/S) ").lower()
    num_set=[i for i in range(1,9)]
    up_alp_set= [ chr(i) for i in range(65,91)]
    random.shuffle(up_alp_set)
    low_alp_set=[ chr(i) for i in range(97,123)]
    random.shuffle(low_alp_set)
    spl_set=["@","$","&", "{", "}", "[", "]", ",", "(", ")","#", "%","?"]
    random.shuffle(spl_set)
    
    password=[0]* length
    index= [i for i in range(0, length)]
    random.shuffle(index)
    
    if mode=="e":
        for i in range(0,length):
            if i <2:
                password[i]= up_alp_set[random.randint(0, len(up_alp_set)-1)]
            elif 2<=i<5:
                password[i]= low_alp_set[random.randint(0, len(low_alp_set)-1)]
            else:
                password[i]= num_set[random.randint(0, len(num_set)-1)]
                     
    elif mode == "m":
        for i in range(0,length):
            if i <3:
                password[index[i]]= num_set[random.randint(0, len(num_set)-1)]
            elif 3<=i<5:
                password[index[i]]= up_alp_set[random.randint(0, len(up_alp_set)-1)]
            else:
                password[index[i]]= low_alp_set[random.randint(0, len(low_alp_set)-1)]

    else:
        for i in range(0,length):
            if i <3:
                password[index[i]]= num_set[random.randint(0, len(num_set)-1)]
            elif 3<=i<5:
                password[index[i]]= up_alp_set[random.randint(0, len(up_alp_set)-1)]
            elif 5<=i<7:
                password[index[i]]= low_alp_set[random.randint(0, len(low_alp_set)-1)]
            else:
                password[index[i]]= spl_set[random.randint(0, len(spl_set)-1)]


    str_password= ''.join(str(i) for i in password)
    print(str_password)
while True:
    generate_password()
    again =input("Press q to quit : ").lower()
    if again=="q":
        break
