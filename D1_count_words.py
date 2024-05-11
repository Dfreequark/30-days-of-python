def count(input_str):
    return len(input_str.split()), len(list(input_str)), len(input_str.split("."))

input_str =input("Enter your string : ")

words, characters, sentences = count(input_str)
print("words: ",words )
print("characters: ", characters )
print("sentences: ",sentences )