'''
Class Inheritance: Create a parent class and multiple child classes demonstrating inheritance and method overriding.

Create a hierarchy of vehicle classes representing different types of vehicles. Include a base class Vehicle and 
derived classes such as Car, Truck, and Motorcycle. 
Each derived class should have attributes and methods specific to that type of vehicle.

'''

class Vehicle():
    def __init__(self, name):
        self.name=name
    
    def info_vehicle(self):
        print("Information of vehicle...")

class Car(Vehicle):
    def __init__(self, name, brand, year):
        super().__init__(name)
        self.brand= brand
        self.year=year
    def info(self):
        super().info_vehicle()
        details={ "Vehicle :":self.name, "Model :": self.brand, "Year of manufacture :": self.year}
        print(details)

vehicle_1= Car("car", "Audi", 2009)
vehicle_2= Car("car", "BMW", 2015)
vehicle_3= Car("car", "Tesla", 2019)

vehicle_1.info()
vehicle_2.info()
vehicle_3.info()