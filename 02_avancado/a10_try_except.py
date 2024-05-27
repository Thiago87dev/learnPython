# The **try** block lets you test a block of code for errors.
# The **except** block lets you handle the error.
# The **else** block lets you execute code when there is no error.
# The **finally** block lets you execute code, regardless of the result of the try- and except blocks.

# The **try** block will generate an exception, because x is not defined

# *********** try... except ***********

try:
    print(x)
except:
    print('x não esta definido jumento')
    
# Print one message if the try block raises a NameError and another for other errors:
try:
    print(x)
except NameError:
    print('A variavel x não esta definida')
except:
    print('Alguma coisa deu errado')
    
# *********** else ***********

# You can use the else keyword to define a block of code to be executed if no errors were raised:

# In this example, the try block does not generate any error:
try:
    print('hello')
except:
    print('Algo deu errado')
else:
    print('Nada deu errado')
    
# *********** finally ***********

# The finally block, if specified, will be executed regardless if the try block raises an error or not
try:
    print(x)
except:
    print('x não esta definido')
finally:
    print('o "try except" terminou')
    
# This can be useful to close objects and clean up resources:

# Try to open and write to a file that is not writable:
try:
    f = open("C:\\Users\\thiag\OneDrive\\Documentos\\New agencia e conta.txt") 
    try:
        f.write('qlq coisa')
    except:
        print('Algo deu errado ao escrever no arquivo') # this except will be executed
    finally:
        f.close()
except:
    print('Algo deu errado ao abrir o arquivo')

# *********** Raise ***********

# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.

# Raise an error and stop the program if x is lower than 0:
# x = -1
# if x < 0:
#     raise Exception('Proibidos numeros menores de zero')

# You can define what kind of error to raise, and the text to print to the user

# Raise a TypeError if x is not an integer:
x = 'hello'
if not type(x) is int:
    raise TypeError('Apenas numeros inteiros são permitidos')