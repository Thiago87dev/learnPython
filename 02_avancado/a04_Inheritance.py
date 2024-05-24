# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# ************** Create a Parent Class **************

# Any class can be a parent class, so the syntax is the same as creating any other class
class Person:
    def __init__(self, fname, lname, sexo):
        self.firstname = fname
        self.lastname = lname

    def printName(self):
        print(self.firstname, self.lastname)

p1 = Person('Bob', 25, 'M')
p1.printName()

# ************** Create a Child Class **************

# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class
class Student(Person):
    pass

# Now the Student class has the same properties and methods as the Person class
s1 = Student('Maria', 21, 'F')

# ************** Add the __init__() Function **************

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function
# The child's __init__() function overrides the inheritance of the parent's __init__() function

class Student(Person):
    def __init__(self, nickname1, nickname12):
        self.nickname1 = nickname1
        self.nickname2 = nickname12
    
    def printnickname(self):
        print(self.nickname1, self.nickname2)

s2 = Student('Harry', 'Potter')
s2.printnickname()
print(s2.nickname1)

# ************** Use the super() Function **************

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent
# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent
class Studend2(Person):
    def __init__(self, fname, lname, sexo, nickname1, nickname2):
        super().__init__(fname, lname, sexo)
        self.nickname1 = nickname1
        self.nickname2 = nickname2

    def printnickname2(self):
        print(self.nickname1, self.nickname2)

s3 = Studend2('Jão', 25, 'M', 'Bob', 'Marley')
s3.printName()
s3.printnickname2()
print(s3.firstname)
