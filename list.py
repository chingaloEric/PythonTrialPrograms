# poor approach of List comprehensions
squares = []
for x in range(10):
    squares.append(x**2)
# print(squares);

# better approach
newSquares = list(map(lambda x: x**2, range(11)))
print(newSquares)

