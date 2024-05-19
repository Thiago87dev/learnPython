# Para adicionar um item ao final da lista, use o método append():
nomes = ['ana', 'maria', 'carla', 'jana']
nomes2 = ['flavia', 'fefa', 'fernanda']
nomes3 = ['joao', 'carlos', 'catia', 'carla', 'carol', 'roberto']
nomes.append('bruna')
print(nomes)

# Para inserir um item de lista em um índice especificado, use o método insert().
nomes.insert(3, 'jessica')
print(nomes)

# Para acrescentar elementos de outra lista à lista atual, use o método extend().
# Com o método extend() você pode adicionar qualquer objeto iterável (listas, tuplas, sets, dicionários etc.).
nomes.extend(nomes2)
print(nomes)

# Extendendo parte de outra lista
nomes.extend(nomes3[2:5])
print(nomes)


t = (1, 2, 3)
t = t + (4, 5)  
print(t)
l = [1, 2, 3]
l.extend([4,5]) 