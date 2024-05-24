frutas = ['banana', 'uva', 'jaca']

for x in frutas:
    print(x)

for x in frutas[1]:
    print(x)

# ********* The range() Function *********
print()
for x in range(6):
    print(x)

print()
for x in range(10, 16):
    print(x)

print()
for x in range(10, 21, 3):
    print(x)

print()
a = 5
for x in range(a):
    print(x)

print()
tamanho = 'tamanho'
for x in range(1,len(tamanho), 2):
    print(x)

# ********* Else in For Loop *********
print()
for x in range(5):
    print(x)
else:
    print('fim do loop for')

# ********* Nested Loops *********  
cor = ['azul', 'rosa', 'roxo']
obj = ['cadeira', 'vaso', 'mesa']

for i in cor:
    for j in obj:
        print(j, i)

def my_function(**kwargs):
  print("His last name is " + kwargs["lname"])

my_function(fname = "Tobias", lname = "Refsnes")