#input_str = input("Enter the line you want to reverse :\n")
input_str= "Hello world, This is Kaushik"

# reversed() => doesn't modify original list/tuple/string
# reverse() => modify original list
print("Reverse through reversed(): ", "".join(reversed(input_str)))

# join a list of elements: "joining space/character".join(list_name)

# slicing: string[ start : end : step_size]
#reverse through slicing: string[::-1]
print("Reversed through slicing:", input_str[::-1])


# spliting the string into words and return as a list: input_str.split()

list_words=input_str.split()
print("Spliting : ", list_words)
print("Join :", ' '.join(list_words))
print("Join through + :", ' + '.join(list_words))

reversed_words= [word[::-1] for word in list_words]
print("Reverse word by word: ", " ".join(reversed_words))
