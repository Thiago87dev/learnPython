# Variavel local e global com o mesmo nome
print('Variavel local e global com o mesmo nome')
x = 'legal'
def minhaFunc ():
    x = 'otimo'
    print('python é ' + x)

minhaFunc()

print('Python é ' + x, end='\n\n')

# Variavel global dentro de uma função
print('Variavel global dentro de uma função')
def minhaFunc2 ():
    global y
    y = 'Espetacular'
    print('python é ' + y)

minhaFunc2()

print('Python é ' + y, end='\n\n')

# use a palavra-chave global se quiser alterar uma variável global dentro de uma função.
z = 'variavel global'

def minhaFunc3 ():
    global z
    z = 'variavel global alterada'

print(z)
minhaFunc3()
print(z)
