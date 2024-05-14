palavras = ['oi', 'teste', 'casa', 'azul', 'gol', 'fui']
numeros = [7, 8, 14]
booleanos = [True, False]
tudo = ['love', 4, True]

print(palavras, numeros, booleanos, tudo)

# Tamanho da lista
print(len(palavras))

# Range indices
print(palavras[1:4]) 
print(palavras[:4], 'pegando desde o inicio até o indice 3') # se não colocar nada no começo ele pega desde o primeiro
print(palavras[2:], 'pegando do indice 2 até o final') # se não colocar nada no final ele pega até o ultimo

# Range de indices negativos
print(palavras[-4:-1])
print(palavras[:-1]) # pegando todos menos o ultimo