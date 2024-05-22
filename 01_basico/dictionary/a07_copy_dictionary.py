pessoa = {
    'nome': 'Bob',
    'idade': 25,
    'cidade': 'Joinville',
    'estado': 'SC',
    'sexo': 'M',
    'profissão': 'cantor',
    'hobby': 'ler'
}

# Você não pode copiar um dicionário simplesmente digitando dict2 = dict1, porque: dict2 será apenas uma referência ao dict1, e as alterações feitas no dict1 também serão feitas automaticamente no dict2

# Existem maneiras de fazer uma cópia, uma maneira é usar o método integrado do Dicionário copy()
pessoa2 = pessoa.copy()

# Outra maneira de fazer uma cópia é usar a função integrada dict()
pessoa3 = dict(pessoa)