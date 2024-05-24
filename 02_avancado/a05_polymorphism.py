# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move()

# Different classes with the same method:
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print('Drive')

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('sail')

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('fly') 

car = Car('Ford', 'Mustang')
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Boeing", "747")

for i in (car, boat, plane):
    i.move()
# Look at the for loop at the end. Because of polymorphism we can execute the same method for all three classes

# ***************** Inheritance Class Polymorphism *****************

# If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:

# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:
print()
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('move!')

class Car2(Vehicle):
    pass

class Boat2(Vehicle):
    def move(self):
        print('sail!')

class Plane2(Vehicle):
    def move(self):
        print('fly!')
    
car2 = Car2('Ford', 'Mustang')
boat2 = Boat2('Ibiza', 'Touring 20')
plane2 = Plane2('Boeing', '747')

for i in (car2, boat2, plane2):
    print(i.brand)
    print(i.model)
    i.move()