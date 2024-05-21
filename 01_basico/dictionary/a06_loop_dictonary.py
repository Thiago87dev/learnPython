pessoa = {
    'nome': 'Bob',
    'idade': 25,
    'cidade': 'Joinville',
    'estado': 'SC',
    'sexo': 'M',
    'profissão': 'cantor',
    'hobby': 'ler'
}

# Você pode percorrer um dicionário usando um loop for
# Ao percorrer um dicionário, o valor de retorno são as chaves do dicionário, mas também existem métodos para retornar os valores
for x in pessoa:
    print(x)

# Imprima todos os valores do dicionário, um por um
for x in pessoa:
    print(pessoa[x])

# Você também pode usar o método values() para retornar valores de um dicionário
for x in pessoa.values():
    print(x)

# Você pode usar o método keys() para retornar as chaves de um dicionário
for x in pessoa.keys():
    print(x)

# Faça um loop pelas chaves e valores, usando o método items()
for x in pessoa.items():
    print(x)

# ou
for x, y in pessoa.items():
    print(x, y)