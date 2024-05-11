original_dict={"a":1, "b":2, "c":3}



def swap(dictionary):
    return {value : key for key, value in dictionary.items()}

swapped_dict= swap(original_dict)
print("Original dictionary is : ", original_dict)
print("Swapped dictionary is : ", swapped_dict)

