i = 1
a = 1
b = 0
c = 1
while i < 6:
    print(i)
    i += 1

# ********* The break Statement *********
print()
while a < 6:
    print(a)
    if a == 3:
        break
    a += 1

# ********* The continue Statement *********
print()
while b < 6:
    b += 1
    if b == 3:
        continue
    print(b)

# ********* The else Statement *********
print()
while c < 6:
    print(c)
    c += 1
else:
    print('acabou o while')