import random
# random.random)()
#Retorne um número float aleatório entre 0.0 e 1.0
print(random.random())

# random.randrange()
# Retorna um número aleatório entre o intervalo fornecido
print(random.randrange(1, 10))

# random.uniform()
# Retorna um número float aleatório entre dois parâmetros fornecidos
print(random.uniform(20, 60))

# random.choice()
#Retorna um elemento aleatório da sequência fornecida
frutas = ['banana', 'uva', 'maça', 'pera', 'goiaba']
print(random.choice(frutas))
x = 'Thiago alves'
print(random.choice(x))

# random.choice()
# weights = Opcional. Uma lista onde você pode avaliar a possibilidade de cada valor. Padrão Nenhum
# k = Opcional. Um número inteiro que define o comprimento da lista retornada. Padrão 1
print(random.choices(frutas, weights=[20,1,1,1,1], k=4))

# random.shuffle()
# reorganizar a ordem dos itens da lista
random.shuffle(frutas)
print(frutas)

# random.sample()
# Retorna uma determinada amostra de uma sequência
print(random.sample(frutas, k=2))