# Subistituindo valor
frutas = ['uva', 'banana', 'pera', 'maça', 'jaca']
frutas [1] = 'goiaba'
print(frutas)

# Alterar um intervalo de valores de itens
frutas[1:3] = ['pessego','laranja'] 
print(frutas)

# Se você inserir mais itens do que propos, os novos itens serão inseridos onde você especificou e os itens restantes serão movidos de acordo (o tamanho da lista ira aumentar)
frutas[1:3] = ['tomate','kiwi','mixirica'] 
print(frutas)

# Se você inserir menos itens do que propos, os novos itens serão inseridos onde você especificou e os itens restantes serão movidos de acordo
frutas[1:3] = ['morango']
print(frutas)

# Para inserir um novo item da lista, sem substituir nenhum dos valores existentes, podemos usar o método insert().
# O método insert() insere um item no índice especificado:
frutas.insert(2, 'Maracuja')
print(frutas)
