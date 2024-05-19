frutas = {'maça', 'uva', 'pera'}
frutas2 = {'banana', 'melao', 'laranja'}

# Para remover um item de um set, use o método remove() ou discard()
# Se o item a ser removido não existir, remove() gerará um erro
frutas.remove('maça')
print(frutas)

#Se o item a ser removido não existir, discard() NÃO gerará um erro
frutas.discard('uva')
print(frutas)

# Você também pode usar o método pop() para remover um item, mas esse método removerá um item aleatório, portanto você não pode ter certeza de qual item será removido.
# O valor de retorno do método pop() é o item removido.
x = frutas2.pop()
print(x)

# O método clear() esvazia o set:
frutas.clear()
print(frutas)

# A palavra-chave del excluirá o conjunto completamente:
del frutas2
