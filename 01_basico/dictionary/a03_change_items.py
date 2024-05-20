carro = {
    'marca': 'ford',
    'modelo': 'ka',
    'ano': 2012,
}
carro['ano'] = 2023
print(carro)

# O método update() atualizará o dicionário com os itens do argumento fornecido
carro.update({'modelo':'fiesta'})
print(carro)
