a = 10
b = 20

print(a > b)
print(a == b)
print(a < b)

if a > b:
    print('A é maior')
elif a == b:
    print('B é igual a A')
else:
    print('B é maior')

# A função bool() permite avaliar qualquer valor e fornecer True ou False em troca
print(bool('oi'))
print(bool(0))

# valore falsos
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# Você pode criar funções que retornem um valor booleano

def boolFunction():
    return True

if boolFunction():
    print('verdadiro')
else:
    print('falso')

# Python também possui muitas funções integradas que retornam um valor booleano, como a função isinstance(), que pode ser usada para determinar se um objeto é de um determinado tipo de dados:

print(isinstance(a, str))