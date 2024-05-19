# Oferece uma sintaxe mais curta quando você deseja criar uma nova lista com base nos valores de uma lista existente.

frutas = ['maça','abacaxi', 'banana', 'jaca', 'amora', 'morango', 'abacate', 'ameixa', 'damasco']

# Frutas que contenham a letra 'm'
frutas_que_tem_M = [x for x in frutas if 'm' in x]
print(frutas_que_tem_M)

# Frutas sem morango
frutas_sem_morango = [x for x in frutas if x != 'morango']
print(frutas_sem_morango)

# Criando uma lista de numeros
numeros = [x for x in range(10)]
print(numeros)

# Criando uma lista com numeros 
numeros_pares = [x for x in range(1, 11) if x %2 == 0]
print(numeros_pares)

# Manipulando expressôes
# Colocando todas as frutas com letras maisuculas
frutas_maiusculas = [x.upper() for x in frutas]
print(frutas_maiusculas)

# Defina todos os valores na nova lista como 'hello'
hello = ['hello' for x in frutas]
print(hello)

# A expressão também pode conter condições, não como um filtro, mas como uma forma de manipular o resultado
macaco_come = [x if x != 'banana' else 'Macaco come' for x in frutas ]
print(macaco_come)

# Frutas que começam com a letra a tem o texto 'começa com a'
comeca_com_A = [x if x[0] != 'a' else 'começa com A' for x in frutas]
print(comeca_com_A)