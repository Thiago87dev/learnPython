a = 10
b = 20
c = 30
# Uma "instrução if" é escrita usando a palavra-chave if
if b > a:
    print('B é maior que A')

if b > a:
    print('B é maior que A')
else:
    print('B não é maior que A')

if b > a:
    print('B é maior que A')
elif a == b:
    print('B é igual A')
else:
    print('A é maior que B')

# *************** AND ***************
if a < b and b < c:
    print('as 2 condiçoes sao verdadeiras')

# *************** OR ***************
if a > b or c > b:
    print('pelo menos uma condição é verdadeira')

# *************** not ***************
if not b > c:
    print('B não é maior que C')

# *************** Short Hand If ***************
if b > a: print('a é maior que b')

print("B") if b > a else print("A")

print("A") if a > b else print('igual') if a == b else print("B")

# *************** Nested If ***************
if c > 5:
    print('maior que 5')
    if c > 10:
        print('maior que 10')
        if c > 20:
            print('maior que 20')

