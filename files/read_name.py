""" File read """

# the package to read the file path
import os.path

# current path
current_path = os.path.abspath(os.path.dirname(__file__))

# appending the file name
path = os.path.join(current_path, "names.txt")

# method to read the file
"""
Python has different file access modes:
'r' = reading
'w' = writing
'x' = creating and writting a file
'a' = appending a file
'r+' = reading and writting a file

"""
with open(path, 'r') as file_object:
    # reading the whole file

    # file_content = file_object.read()
    # print(file_content)

    # reading line by line
    names = []
    for line in file_object:
        names.append(line.strip())
    
    for name in names:
        print('Hello, my name is ' + name)