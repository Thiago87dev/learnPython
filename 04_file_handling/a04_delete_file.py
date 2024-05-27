# To delete a file, you must import the OS module, and run its os.remove() function:
import os

# ************* Check if File exist *************
if os.path.exists('myfile.txt'):
    os.remove('myfile.txt')
else:
    print('the file does not exist')
    
# ************* Delete Folder *************

# To delete an entire folder, use the os.rmdir() method:
# Note: You can only remove empty folders.

# os.rmdir('myfolder')