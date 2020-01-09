""" File read """

# the package to read the file path
import os.path

# current path
current_path = os.path.abspath(os.path.dirname(__file__))

file_name = input('Please write the name of file to be read. \n(With the extension): ')

# appending the file name
path = os.path.join(current_path, file_name)

# method to read the file
"""
Python has different file access modes:
'r' = reading
'w' = writing
'x' = creating and writting a file
'a' = appending a file
'r+' = reading and writting a file

"""
try: 
    with open(path, 'r') as file_object:
    # reading the whole file

        # file_content = file_object.read()
        # print(file_content)

        # reading line by line
        names = []
        for line in file_object:
            names.append(line.strip())
        print('\nPrinting the content of :' + file_name + '\n')
        for name in names:
            print('Hello, my name is ' + name)
except FileNotFoundError:
    print('File with name ' + file_name + ', is Not found on current directory')