from floodfill import floodFill
matrix = [[0, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0]]
y, x, new = 0, 0, 2
result = floodFill(matrix, y, x, new)
print('Input:', '\n'.join(str(m) for m in matrix), 'Fill from [{0}, {1}]:'.format(y, x), '\n'.join(str(r) for r in result), sep = '\n')