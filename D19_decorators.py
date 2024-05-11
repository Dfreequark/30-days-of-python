def create_adder(x): 
    def adder(y): 
        return x+y 
 
    return adder 
 
add_15 = create_adder(15) # add_15 is a variable storing a function adder
 
print(add_15(10)) 


print("--------------------------------")

def hello_decorator(func):
	def inner1(*args, **kwargs):
		
		print("before Execution")
		
		# getting the returned value
		returned_value = func(*args, **kwargs)
		print("after Execution")
		
		# returning the value to the original frame
		return returned_value
		
	return inner1


# adding decorator to the function
@hello_decorator                # equivalent to : sum= hello_decorator(sum_two_numbers)
def sum_two_numbers(a, b):
	print("Inside the function")
	return a + b


a, b = 1, 2

#sum = hello_decorator(sum_two_numbers)
# getting the value through return of the function
print("Sum =", sum(a, b))
