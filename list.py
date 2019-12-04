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

# list comprehensions
squares = [num**2 for num in range(1,11)]
print(squares)