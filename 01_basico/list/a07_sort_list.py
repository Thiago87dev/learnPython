# Os objetos de lista possuem um método sort() que classificará a lista alfanumericamente, em ordem crescente, por padrão

frutas = ['maça','abacaxi', 'banana', 'jaca', 'amora', 'morango', 'abacate', 'ameixa', 'damasco']
numeros = [10, 7, 4, 15, 27, 31, 115]

frutas.sort()
print(frutas)

numeros.sort()
print(numeros)

# Para classificar em ordem decrescente, use o argumento de palavra-chave reverse = True
frutas.sort(reverse=True)
print(frutas)

numeros.sort(reverse=True)
print(numeros)

# Você também pode personalizar sua própria função usando a palavra-chave argumento key = function.
# A função retornará um número que será usado para ordenar a lista (primeiro o número mais baixo)
# Classifique a lista com base em quão próximo o número está de 50
def myfunc(n):
    return abs(n - 50)

lista = [100, 50, 65, 82, 23]
lista.sort(key=myfunc)
print(lista)

# Case Insensitive Sort
# Por padrão, o método sort() diferencia maiúsculas de minúsculas, resultando em todas as letras maiúsculas sendo classificadas antes das letras minúsculas
# Felizmente, podemos usar built-in functions como key functions ao classificar uma lista
frutas2 = ['Jaca', 'banana', 'damasco', 'Uva']
frutas2.sort(key=str.lower)
print(frutas2)

# Apenas revertendo a ordem existente
frutas3 = ['Jaca', 'banana', 'damasco', 'Uva', 'kiwi']
frutas3.reverse()
print(frutas3)