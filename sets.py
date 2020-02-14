'''
Sets have the following properties:
    1. Collection of elements in unordered
    2. No duplicate elements can be stored
    3. Sets are mutable
'''
# created sets
languages = set()
names = {'Eric', 'Lisa'}
print(names)

# adding elements to set
languages.add('Python')
languages.add('Java')
languages.add('php')
# adding multiple elements
languages.update(['C', 'Javascript'])

'''
removing specific element in set
'''
# if an element specified is not found, the function does nothing
languages.discard('Javaa')
# if an element is not found raises keyError
languages.remove('Java')

# removing the last element of the set
languages.pop()
print(languages)

# removed all elements in set
languages.clear()

# coping a set
new_names = names.copy()
print(new_names)

# max element
num = {1, 3, 10, 2, 5}
print(max(num))

# min element
print(min(num))

# number of elements in the set
print(len(num))

# sort the set
sorted_num = sorted(num)
print(sorted_num)

# sum of elements
print(sum(sorted_num))

'''
Set operation invloving multiple sets
'''
num_set_1 = set([1, 2, 30, 48, 10])
num_set_2 = set([1, 10, 43, 55, 100, 39 , 13])

# difference between sets
# A.difference(B) returns element in A but not B
print(num_set_2.difference(num_set_1))
# find difference and update the set
# num_set_2.difference_update(num_set_1)
# print(num_set_2)

# to find symmetric difference
print(num_set_2.symmetric_difference(num_set_1))
# find difference and update the set
# num_set_2.symmetric_difference_update(num_set_1)
# print(num_set_2)

# to find intersection
print(num_set_1.intersection(num_set_2))
# to find intersection and update the set
# num_set_1.intersection_update(num_set_2)
# print(num_set_1)

# to find union
print(num_set_1.union(num_set_2))
# to find intersection and update the set
# num_set_1.update(num_set_2)
# print(num_set_1)

# check disjoint
print(num_set_1.isdisjoint(num_set_2))

# check subset
print(num_set_1.issubset(num_set_2))

# check superset
print(num_set_1.issuperset(num_set_2))

