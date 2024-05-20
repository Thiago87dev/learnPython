# Você pode acessar os itens de um dicionário referindo-se ao nome da chave, entre colchetes
carro = {
    'marca': 'ford',
    'modelo': 'ka',
    'ano': 2012,
}
x = carro['ano']
print(x)

# Existe também um método chamado get() que lhe dará o mesmo resultado
x = carro.get('modelo')
print(x)

# ************* Obtendo chaves *************

# O método keys() retornará uma lista de todas as chaves do dicionário.
x = carro.keys()
print(x)

# A lista de chaves é uma visualização do dicionário, o que significa que quaisquer alterações feitas no dicionário serão refletidas na lista de chaves.

carro['cor'] = 'branco'
print(x) # após a mudança

# ************* Obtendo valores *************

# O método values() retornará uma lista de todos os valores do dicionário.
x = carro.values()
print(x) # após a mudança

# A lista de valores é uma visualização do dicionário, o que significa que quaisquer alterações feitas no dicionário serão refletidas na lista de valores.
carro['cor'] = 'preto'
print(x) # após a mudança

# ************* Obtendo itens *************

# O método items() retornará cada item de um dicionário, como tuplas em uma lista
x = carro.items()
print(x)

# A lista retornada é uma visualização dos itens do dicionário, o que significa que quaisquer alterações feitas no dicionário serão refletidas na lista de itens.
carro['placa'] = 'abc1234'
print(x) # após a mudança

# ************* Verifique se a chave existe *************

# Para determinar se uma chave especificada está presente em um dicionário, use a palavra-chave in
if 'placa' in carro:
    print('sim, a placa esta cadastrada')