# poor approach of List comprehensions
squares = []
for x in range(10):
    squares.append(x**2)
# print(squares);

# better approach
newSquares = list(map(lambda x: x**2, range(11)))
# print(newSquares)

just_list = [1, 'Eric']
# print(len(just_list))

names = ['Eric', 'Lisa']
message = 'Hello'
for count in range(len(names)):
    # print(message + " " + names[count])
    pass

# copying the list
new_names = names[:]
print(new_names)

# list comprehensions
squares = [num**2 for num in range(1,11)]
print(squares)

# It is advised to use 'while' loop to modiffy the list
# deleting an item:
users = ['eric', 'josh', 'lisa']
to_be_deleted = 'josh'
while to_be_deleted in users:
    users.remove(to_be_deleted)

print(users)