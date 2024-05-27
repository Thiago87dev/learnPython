nome = 'Thiago Alves'
nome_sem_espaco = ''

for i in nome:
    if i != ' ':
        nome_sem_espaco += i

print(nome_sem_espaco)

# Melhor forma
nome = nome.replace(' ', '')
print(nome)