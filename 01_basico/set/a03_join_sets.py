frutas = {'maça', 'uva', 'pera'}
frutas2 = {'banana', 'melao', 'laranja'}
nomes = {'ana', 'bob', 'maria'}
nomes2 = {'bob', 'carla', 'rose'}
nomes3 = {'ana', 'carla', 'bob'}
numeros = {1, 2, 3}
numeros2 = {4, 5, 6}

# ******** union() ********

# O método union() retorna um novo set com todos os itens de ambos os sets.
frutas3 = frutas.union(frutas2)
print(frutas3)

# Você pode usar o operador | em vez do método union(), e você obterá o mesmo resultado.
numeros3 = numeros | numeros2
print(numeros3)

# Todos os métodos e operadores de união podem ser usados ​​para unir vários sets. 
# Ao usar um método, basta adicionar mais sets entre parênteses, separados por vírgulas:

mistura = frutas.union(frutas2, numeros, numeros2)
print(mistura)

# Ao usar o operador |, separe os sets com mais | operadores:
mistura2 = frutas | frutas2 | numeros | numeros2
print(mistura)

# OBS: O método union() permite unir um sets com outros tipos de dados, como listas ou tuplas.
# Mas O operador | só permite unir sets com sets, e não com outros tipos de dados, como é possível com o método union().

# ******** update() ********

# O método update() insere todos os itens de um set em outro.
frutas2.update(frutas)
print(frutas2)

# OBS: Tanto union() quanto update() excluirão quaisquer itens duplicados.

# ******** intersection() ********

# O método intersection() retornará um novo set, que contém apenas os itens que estão presentes em ambos os sets.
nomes4 = nomes.intersection(nomes2)
print(nomes4)

# Você pode usar o operador & em vez do método intersection() e obterá o mesmo resultado.
nomes5 = nomes.intersection(nomes2)
print(nomes5)

# OBS: O operador & permite apenas unir sets com sets, e não com outros tipos de dados como você pode fazer com o métodosection().

# O método intersection_update() também manterá SOMENTE as duplicatas, mas alterará o set original em vez de retornar um novo set.
nomes.intersection_update(nomes2)
print(nomes)

# OBS: Os valores True e 1 são considerados o mesmo valor. O mesmo vale para False e 0.

# ******** difference() ********

# O método Difference() retornará um novo set que conterá apenas os itens do primeiro set que não estão presentes no outro set.

nomes6 = nomes2.difference(nomes3)
print(nomes6)

# Você pode usar o operador - em vez do método Difference() e obterá o mesmo resultado.
nomes7 = nomes2 - nomes3
print(nomes7)

# O método Difference_update() também manterá os itens do primeiro set que não estão no outro set, mas alterará o set original em vez de retornar um novo set.
nomes2.difference_update(nomes3)

# ******** symmetric_difference() ********

# O método symmetric_difference() manterá apenas os elementos que NÃO estão presentes em ambos os sets.
