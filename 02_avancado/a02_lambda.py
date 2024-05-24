#A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Add 10 to argument a, and return the result
add10 = lambda a : a + 10
print(add10(5))

# Multiply argument a with argument b and return the result
soma = lambda a, b : a + b
print(soma(10, 20))

# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
# Use that function definition to make a function that always doubles or triples the number you send in:
def myfunc(n):
    return lambda a : a * n

mydobubler = myfunc(2)
print(mytripler(11))

mytripler = myfunc(3)
print(mydobubler(11))