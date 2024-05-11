#uses of lambda function = f(x)

y = lambda x : x + 10   # y= f(x)= x+10
print(y(2))

double = lambda x: x*2
print(double(4))

magnitude = lambda x, y : (x**2 + y**2)**0.5
print(magnitude(3,4))


#uses of lambda function in other functions as an argument

#sort(list, key= function)
a=[1,-5,-3,2,4]
print("a= ", a)
print("Sorted a =", sorted(a))
print("Sorted a with magnitude=", sorted(a, key = lambda x: abs(x)))
a.sort()
print("Sorted a =", a)

a.sort(reverse= True)
print("Reverse sorted a =", a)


c= [(2,1), (5, -1), (-2, 9), (0,3)]
print("Sorted c with x:", sorted(c))
print("Sorted c with y:", sorted(c, key = lambda x: x[1]))
print("Sorted c with x+y:", sorted(c, key = lambda x: x[0]+x[1]))

#map(key, list) => returns an object

d= [1,2,3,4,5]
double_list = list(map(lambda x : x *2, d))
print("Double of d = ", double_list)

print("a= ", a, " ;\n d= ", d)
print(list(map(lambda x, y: x+ y, a,d)))

#filter(key, list)
e= [1,-2,3,4,5,6]
print("Even = ",list(filter(lambda x: x%2==0, e)), "\n Odd = ", list(filter(lambda x: x%2==1, e)))

positive = list(filter(lambda x: x>0, e))
print("Positive of e =", positive)
