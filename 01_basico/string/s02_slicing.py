# Você pode retornar um intervalo de caracteres usando a sintaxe de fatia.

# Especifique o índice inicial e o índice final(não incluso), separados por dois pontos, para retornar uma parte da string.

a = 'Meu nome é Thiago'
print(a[4:8])

# Fatie desde o início
print(a[:8])

# Fatie até o fim
print(a[11:])

# indices negativos
# Use índices negativos para iniciar a fatia do final da string:
# -1 é a ultima posição
print(a[-1])
print(a[-6:])
print(a[-13:-9])