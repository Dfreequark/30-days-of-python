# iterator

string ="Hello World"
str_iter= iter(string)

for x in string:    #for converts string to str_iter internally
    print(x)
print("---------")

#for x in str_iter:  #same as above
#    print(x)



# generator => returns an iterator

def numbers():
    yield 1
    yield 2
    yield 3

for i in numbers():   # here numbers() = an iterator
    print(i)

print("---------")

def even_gen(limit):
    for i in range(1,limit):
        if i%2==0:
            yield i

for even in even_gen(11):
    print(even)

print("---------")

# fibonacci using generator

def fibo(limit):
    a, b= 0, 1
    
    while a < limit:
        yield a
        a , b = b, a+b

fibo_iter= fibo(30)
for num in fibo_iter:
    print(num)
    if num ==5: 
        break
print("--------")

print(next(fibo_iter))
print(next(fibo_iter))
print(next(fibo_iter))