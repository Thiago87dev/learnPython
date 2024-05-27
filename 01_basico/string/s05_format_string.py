# F-Strings

# Basta colocar um f na frente da string literal e adicionar colchetes {} como espaços reservados para variáveis ​​e outras operações.

# Um espaço reservado pode conter variáveis, operações, funções e modificadores para formatar o valor.

idade = 25
texto = f'Minha idade é {idade}'
print(texto)

preco = 29
texto = f'O preço é {preco} reais'
print(texto.upper())

# Um modificador é incluído adicionando dois pontos ':' seguido por um tipo de formatação legal, como '.2f' que significa número de ponto fixo com 2 casas decimais
print(f'O preço é {preco:.2f} reais')

# Um espaço reservado pode conter código Python, como operações matemáticas
print(f'O preço é {29 + 50}')

texto = 'Eu tenho {} anos'
print(texto.format(idade))

fruta = 'banana'
print(f'minha fruta favorita é {fruta.upper()}')