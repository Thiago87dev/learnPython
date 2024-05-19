# Você pode percorrer os itens da lista usando um loop for:
frutas = ['uva','banana', 'pera', 'jaca', 'melao']

for i in frutas:
    print(i)

print('********** 2')
# Você também pode percorrer os itens da lista consultando seu número de índice.
# Use as funções range() e len() para criar um iterável adequado.
for i in range(len(frutas)):
    print(frutas[i])

print('********** 3')
# Você pode percorrer os itens da lista usando um loop while.
i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1

print('********** 4')
# Loop usando List Comprehension
[print(x) for x in frutas]
