import os.path

name = input('Enter a name: ')

path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(path, "names.txt")

# with 'w' mode, if a file is no there it's created
# with open(path, 'w') as file_object:
    # file_object.write(name + '\n')

# with append method, we dont overwrite the existing data, also if file is not there, it,s created
with open(path, 'a') as file_object:
    file_object.write(name + '\n')