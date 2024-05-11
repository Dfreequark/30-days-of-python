

'''foods = list()
while True:
  food = input("What food do you like?: ")
  if food == "quit":
    break
    foods.append(food)
 
# Below Approach uses Walrus Operator
foods = list()
while (food := input("What food do you like:=  ")) != "quit":
    foods.append(food)
print(foods)
'''


numbers = [1, 2, 3, 4, 5]

 
while (last := len(numbers)) > 0:
    numbers.pop()

print(last)