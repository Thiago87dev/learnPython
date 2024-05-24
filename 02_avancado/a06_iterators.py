# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

# ************* Iterator vs Iterable *************

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:

# Return an iterator from a tuple, and print each value:

frutas = ('banana', 'uva', 'maça')
myit = iter(frutas)

print(next(myit))
print(next(myit))
print(next(myit))

# Even strings are iterable objects, and can return an iterator:
# Strings are also iterable objects, containing a sequence of characters:

fruta = 'banana'
myit = iter(fruta)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# ************* Create an Iterator *************

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.

# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# ************* StopIteration *************

# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
# To prevent the iteration from going on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times

# Stop after 20 iterations:
class MyNumbers2:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else: raise StopIteration

myclass2 = MyNumbers2()
myiter2 = iter(myclass2)

for i in myiter2:
    print(i)