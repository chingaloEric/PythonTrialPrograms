''''
Using if conditions with lists
'''

names = []
if names: 
    print(names)
else:
    print('no names')

names = ['Lisa', 'Eric', 'Antonela']
requested_name = 'Lisa'

# checking a name in list of names
if requested_name in names:
    print('Found ' + requested_name)
else:
    print('Names Not Found')