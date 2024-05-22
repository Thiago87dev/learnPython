filhos = {
    "filho 1": {
        'nome': 'Yasmin',
        'idade': 13,

    },
    'filho 2':{
        'nome': 'Nathan',
        'idade': 8
    },
    'filho 3': {
        'nome': 'N/A',
        'idade': 0,
    },
}
print(filhos)

# Ou, se quiser adicionar três dicionários a um novo dicionário:

filho1 = {
    'nome': 'Yasmin',
    'idade': 13,
}
filho2 = {
    'nome': 'Nathan',
    'idade': 8
}
filho3 = {
    'nome': 'N/A',
    'idade': 0,
}

meus_filhos = {
    'filho 1': filho1,
    'filho 2': filho2,
    'filho 3': filho3,
}
print(meus_filhos)

# ************** Acessar itens em dicionários aninhados **************

# Para acessar itens de um dicionário aninhado, você usa o nome dos dicionários, começando pelo dicionário externo
print(meus_filhos['filho 2']['nome'])
print()

# ************** Loop através de dicionários aninhados **************

# Você pode percorrer um dicionário usando o método items() assim:
for k, v in meus_filhos.items():
    print(k)
    for k2 in v:
        print(k2 + ':', v[k2])