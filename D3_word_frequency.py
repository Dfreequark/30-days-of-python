
def frequency(input_str):
    words = input_str.lower().split()
    freq_dict ={}
    for word in words:
        if word in freq_dict:
            freq_dict[word] +=1
        else:
            freq_dict[word] =1  
    
        
    return freq_dict

'''input_list=input("enter a string : ")

freq_dic= frequency(input_list)
print("Frequency dictionary :", freq_dic)

'''