# James Aho
# 2/21/2025
# Module 3 Lab - Case Study: Lists, Functions, and Classes: This program demonstrates my understanding of classes, superclasses and the
# idea of inheritance. Asks the user input for information on a vehicle which is saved to a list, then from there the list is
# used to create an object of the automobile class which is then printed.

class Vehicle:
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    def __str__(self):
        return f"The vehicle in question is a {self.year} {self.make} {self.model} that has {self.doors} doors and has a {self.roof} roof. It's classified as a {self.type}"

car = []
car.append(input("Enter the type of vehicle; 'car, truck, plane, boat, or broomstick': "))
car.append(input("Enter the year of your vehicle: "))
car.append(input("Enter the make of your vehicle: "))
car.append(input("Enter the model of your vehicle: "))
car.append(input("Enter the number of doors on your vehicle: "))
car.append(input("Enter the type of sunroof you have on your vehicle; 'solid, sun roof': "))

car = Automobile(car[0], car[1], car[2], car[3], car[4], car[5],)

print(f"Vehicle Type: {car.type.capitalize()}")
print(f"Year: {car.year.capitalize()}")
print(f"Make: {car.make.capitalize()}")
print(f"Model: {car.model.capitalize()}")
print(f"Number Of Doors: {car.doors.capitalize()}")
print(f"Type Of Roof: {car.roof.capitalize()}")


