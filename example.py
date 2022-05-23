from floodfill import floodFill
from random import choice

rows, cols = 5, 5
matrixValues = [0, 1]
matrix = [[choice(matrixValues) for c in range(cols)] for r in range(rows)]

y, x = 0, 0
new = 2

result = floodFill(matrix, y, x, new)
print('Input:', '\n'.join(str(m) for m in matrix), 'Fill from [{0}, {1}]:'.format(y, x), '\n'.join(str(r) for r in result), sep = '\n')
