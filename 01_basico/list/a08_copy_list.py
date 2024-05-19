# Você não pode copiar uma lista simplesmente digitando lista2 = lista1, porque: lista2 será apenas uma referência à lista1, e as alterações feitas na lista1 serão automaticamente feitas também na lista2.

numeros = [10, 7, 4, 15, 27, 31, 115]
numeros_copiados = numeros.copy()
print(numeros_copiados)

# ou
numeros_copiados2 = list(numeros)
print(numeros_copiados2)
