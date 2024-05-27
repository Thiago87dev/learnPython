# ************* Write to an Existing File *************

# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

f = open('teste.txt','a')
f.write('. Now the file has more content')
f.close()
f = open('teste.txt', 'r')
print(f.read())

f2 = open('teste.txt','w')
f2.write('Woops! I have deletd the content.')
f.close()
f2 = open('teste.txt','r')
print(f2.read())

# ************* Create a New File *************

# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

f3 = open('myfile.txt', 'x') # returns an error if the file exist
f4 = open('teste2','w') # returns an error if the file exist