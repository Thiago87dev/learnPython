print('Hello')
print("'hello'") # strint dentro de aspas

# string Multiline 
texto = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(texto)

# string são arrays
a = 'hello world'
print(a[1])

# Loop através de uma string
for x in 'banana':
    print(x)

# Tamanho da string
b = 'Thiago Alves'
print(len(b))

# Checando se existe uma string
txt = "the best things is in life are free"
if 'free' in txt:
    print("Yes, 'free' is present")

# Checando se NÃO existe uma string
txt2 = 'Escrevendo qualquer coisa'
if 'teste' not in txt2:
    print('teste não esta na frase')