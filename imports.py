# import the whole module / file
import functions
print(functions.populate_user('Lisa', 'Tibenda', age=22))

# import a module with an alias
import functions as fn
print(fn.populate_user('Miguel', 'Eric', age=2))

# importing all functions in a module
# from functions import *

# import specific function
from functions import fibonacci
fibonacci(100)

# importing specific functions with an alias
from functions import fibonacci2 as fb
print(fb(100))