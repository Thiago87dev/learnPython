f = open('teste.txt', 'r')
f2 = open('teste.txt', 'r')
f3 = open('teste.txt', 'r')
f4 = open('teste.txt', 'r')

print(f.read())
print()
# Read Only Parts of the File
print(f2.read(5))
print()

# Read Lines
print(f3.readline()) # fist line
print(f3.readline()) # second line

# By looping through the lines of the file, you can read the whole file, line by line:
for i in f4:
    print(i)
    
# Close Files
f.close()
f2.close()
f3.close()
f4.close()