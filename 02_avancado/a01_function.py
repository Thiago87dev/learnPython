def my_func():
    print('Eu sou uma função')

my_func()

def func_nome(nome):
    print(f'meu nome é {nome}')

func_nome('Thiago')

def func_nome_comp(fname, lname):
    print(f'meu nome completo é {fname} {lname}')

func_nome_comp('Thiago', 'Alves')

# ************ *args ************

def meus_filhos(*args):
    print(f'o filho mais novo é o {args[1]}')

meus_filhos('Yasmin', 'Nathan')

# ************ Argumentos nomeados ************

def nome_pessoas(pessoa1, pessoa2, pessoa3):
    print(f'a primeira pessoa é {pessoa1}')

nome_pessoas(pessoa3 = 'ana', pessoa2='Carol', pessoa1='Maria')

# ************ *kwargs ************

def cidades(**kwargs):
    print('Minha cidade é ' + kwargs['cidade1'])

cidades(cidade1 = 'Joinville', cidade2 = 'Floripa')

# ************ Default Parameter Value ************

def minha_func(pais = 'Brasil'):
    print(f'meu pais natal é {pais}')

minha_func('Russia')
minha_func()

# ************ Return Values ************

def soma(a, b):
    return a + b

print(soma(10,5))

# ************ Positional-Only Arguments ************

def soma2(a, b, /):
    return a + b

print(soma2(5, 2))

# ************ Keyword-Only Arguments ************

def soma3(*, a, b):
    return a + b

print(soma3(a=9, b=5))

# ************ Combine Positional-Only and Keyword-Only ************

def soma4(a, b, /, *, c, d):
    return a + b + c + d

print(soma4(4, 2, c=7, d=10))

# ************ Recursion ************
print()
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

tri_recursion(6)