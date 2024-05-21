pessoa = {
    'nome': 'Bob',
    'idade': 25,
    'cidade': 'Joinville'
}

# A adição de um item ao dicionário é feita usando uma nova chave de índice e atribuindo um valor a ela:
pessoa['estado'] = 'SC'
print(pessoa)

# O método update() atualizará o dicionário com os itens de um determinado argumento. Se o item não existir, o item será adicionado.
pessoa.update({'sexo': 'M'})
print(pessoa)
