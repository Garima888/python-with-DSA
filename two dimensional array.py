# 2D Array (Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing an element
print(matrix[1][2])  # Output: 6

# Traversing a 2D array
for row in matrix:
    for element in row:
        print(element, end=' ')  # Output: 1 2 3 4 5 6 7 8 9
    print()  # New line after each row
