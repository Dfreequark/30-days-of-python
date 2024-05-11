'''
Problem (Intermediate - OOP):
Implement a class called Rectangle with attributes length and width. 
Include methods to calculate the area and perimeter of the rectangle.
'''

class Rectangle():

    def __init__(self, length, width):
        self.length= length
        self.width= width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2*(self.length + self.width)
    
rect_1 = Rectangle(2,4)
rect_2 = Rectangle(5,5)
print(f"Area of rect_1 is {rect_1.area()}, perimeter is {rect_1.perimeter()}")
print(f"Area of rect_2 is {rect_2.area()}, perimeter is {rect_2.perimeter()}")