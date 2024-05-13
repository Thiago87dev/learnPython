# Python possui um conjunto de métodos integrados que você pode usar em strings.

texto = 'Meu nome é Thiago Alves, e o nome da minha cidade é São Paulo  '
palavra = 'banana2'
numerosInt = '123456'
numerosFloat = '145.20'
frutas = ['uva', 'jaca', 'maça']

# use para se localizar
print('******************************') 

# Todas maiusculas
print(texto.upper())

# Todas minusculas
print(texto.lower())

# Minúsculas tornam-se maiúsculas e vice-versa
print(palavra.swapcase())

# Primeira letra maiuscula
print(texto.capitalize())

# Converte o primeiro caractere de cada palavra para maiúscula
print(texto.title())

# Removendo espaço do começo e do final do texto
print(texto.strip())

# Substituir string
print(texto.replace('o', '8'))

# Separando string -> retorna um ARRAY
print(texto.split(','))

# Une os elementos de um iterável ao final da string
print('---'.join(frutas))

# Retorna uma string centralizada (palavra unica)
print(palavra.center(10, '*'))

# Retorna o número de vezes que um valor especificado ocorre em uma string
print(texto.count('a'))

# Retorna verdadeiro se a string terminar com o valor especificado
print(palavra.endswith('a'))

# Retorna verdadeiro se a string começar com o valor especificado
print(palavra.startswith('b'))

# Pesquisa a string por um valor especificado e retorna a posição onde ele foi encontrado
print(texto.index('nome'))

# Pesquisa a string por um valor especificado e retorna a última posição de onde foi encontrado
print(texto.rindex('nome'))

# Retorna True se todos os caracteres da string forem alfanuméricos
print(palavra.isalnum())

# Retorna True se todos os caracteres da string estiverem no alfabeto
print(palavra.isalpha())

# Retorna True se todos os caracteres da string forem caracteres ASCII
print(palavra.isascii())

# Retorna True se todos os caracteres da string forem decimais
print(numerosInt.isdecimal())

#Retorna True se todos os caracteres da string forem dígitos
print(numerosInt.isdigit())

# Retorna True se todos os caracteres da string forem numéricos
print(numerosInt.isnumeric())

# Returns True if all characters in the string are lower case
print(palavra.islower())

# Retorna True se todos os caracteres da string estiverem maiúsculos
print(palavra.isupper())

# Retorna uma tupla onde a string é dividida em três partes
print(texto.partition('nome'))

# Preenche a string com 0 no inicio ate a string atingir o tamanho especificado
print(palavra.zfill(10))