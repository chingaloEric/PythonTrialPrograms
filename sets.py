'''
Sets have the following properties:
    1. Collection of items in unordered
    2. No duplicate items can be stored
    3. Sets are mutable
'''
# created sets
languages = set()
names = {'Eric', 'Lisa'}
print(names)

# adding items to set
languages.add('Python')
languages.add('Java')

'''
removing specific item in set
'''
# if an item specified is not found, the function does nothing
languages.discard('Javaa')
# if an item is not found raises keyError
languages.remove('Java')

# removing the last item of the set
languages.pop()
print(languages)

# removed all items in set
languages.clear()

# coping a set
new_names = names.copy()
print(new_names)

# max item
num = {1, 3, 10, 2, 5}
print(max(num))

# min item
print(min(num))

# number of items in the set
print(len(num))

# sort the set
sorted_num = sorted(num)
print(sorted_num)

# sum of items
print(sum(sorted_num))