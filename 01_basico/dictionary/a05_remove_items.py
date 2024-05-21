pessoa = {
    'nome': 'Bob',
    'idade': 25,
    'cidade': 'Joinville',
    'estado': 'SC',
    'sexo': 'M',
    'profissão': 'cantor',
    'hobby': 'ler'
}

# O método pop() remove o item com o nome de chave especificado:
pessoa.pop('idade')
print(pessoa)

# O método popitem() remove o último item inserido
pessoa.popitem()
print(pessoa)

# A palavra-chave del remove o item com o nome de chave especificado
# A palavra-chave del também pode excluir completamente o dicionário
# del pessoa
del pessoa['sexo']
print(pessoa)

# O método clear() esvazia o dicionário
pessoa.clear()
print(pessoa)