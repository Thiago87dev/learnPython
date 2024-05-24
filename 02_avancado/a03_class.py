# Create a class named MyClass, with a property named x
class MyClass:
    x = 5

# Now we can use the class named MyClass to create objects
p1 = MyClass()
print(p1.x)

# ************* __init__() Function *************

# All classes have a function called __init__(), which is always executed when the class is being initiated
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created

# Create a class named Person, use the __init__() function to assign values for name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Bob', 25)
p2 = Person('Carol', 21)
print(p1.name, p1.age)
print(p2.name, p2.age)

# ************* __str__() Function *************

# The __str__() function controls what should be returned when the class object is represented as a string
# If the __str__() function is not set, the string representation of the object is returned

# The string representation of an object WITHOUT the __str__() function
class OtherPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = OtherPerson('Ted', 20)
print(p1)

# The string representation of an object WITH the __str__() function:
class OtherPerson2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} ({self.age})'

p1 = OtherPerson2('Ted', 20)
print(p1)

# ************* Object Methods *************

# Objects can also contain methods. Methods in objects are functions that belong to the object.

# Insert a function that prints a greeting, and execute it on the p1 object:

class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def sayHello(self):
    print(f'Hello my name is {self.name}')

p1 = Person2('Bruna', 22)
p1.sayHello()

# ************* The self Parameter *************

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

class Car:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def carYear(self):
        print(f'o ano do carro é {self.year}')

c1 = Car('Mustang', 1998)
c1.carYear()

# ************* Modify Object Properties *************

c1.year = 2023
c1.carYear()

# ************* Delete Object Properties *************

del c1.name

# ************* Delete Objects *************

del c1