a = 5 # int
b = 5.5 # float
c= 'oi' # string
d = True # boolean

# Se você quiser especificar o tipo de dados de uma variável, isso pode ser feito com conversão:
e = str(3) # sera uma string '3'
f = float(3) # sera float 3.0
g = int(3) # sera int 3

# descobrindo o tipo:
h = 5
i = 'teste'
print('tipos')
print(type(h))
print(type(i), end='\n\n')

# as variaveis são case sensitive:
j = 10 # esse j minusculo é uma variavel
J = 5 # e esse J maiusculo e outra variavel

#atribuindo valores a múltiplas variáveis ​​em uma linha:
k, l , m = 'banana', 'maça', 'uva'

#atribuindo o mesmo valor a múltiplas variáveis ​​em uma linha:
n = o = p = 'Manga'

# Se você tiver uma coleção de valores em uma lista, tupla etc. Python permite extrair os valores em variáveis. Isso é chamado de descompactação:
frutas = ['pera','goiaba','jaca']
q, r, s = frutas
print('unpacking')
print(r, end='\n\n' )