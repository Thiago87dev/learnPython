lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]

# Uma das maneiras mais fáceis é usar o operador +.
lista3 = lista1 + lista2
print(lista3)

# Outra forma de unir duas listas é anexar todos os itens da lista2 à lista1, um por um:
for x in lista2:
    lista1.append(x)
print(lista1)

# Ou você pode usar o método extend(), onde o objetivo é adicionar elementos de uma lista a outra lista
lista1.extend(lista2)
print(lista1)
