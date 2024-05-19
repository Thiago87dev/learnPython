# O método remove() remove o item especificado.
# Se houver mais de um item com o valor especificado, o método remove() remove a primeira ocorrência:
nomes = ['ana', 'joana', 'dai', 'carla', 'maria', 'carol', 'deb', 'flavia', 'bruna']
nomes.remove('dai')
print(nomes)

# O método pop() remove o índice especificado.
# Se você não especificar o índice, o método pop() removerá o último item.
nomes.pop(1)
print(nomes)

nomes.pop()
print(nomes)

# A palavra-chave del também remove o índice especificado:
# A palavra-chave del também pode excluir a lista completamente.
del nomes[1]
print(nomes)

# O método clear() esvazia a lista.
nomes.clear()
print(nomes)

