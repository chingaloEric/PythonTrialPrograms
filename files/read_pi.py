""" File read """

# the package to read the file path
import os.path

# current path
current_path = os.path.abspath(os.path.dirname(__file__))

# appending the file name
path = os.path.join(current_path, "names.txt")

# method to read the file
with open(path, 'r') as file_object:
    file_content = file_object.read()
    print(file_content)