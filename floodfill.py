def floodFill(matrix, y, x, new):
    result = [row[:] for row in matrix]
    rows = len(result)
    cols = len(result[0])
    old = result[y][x]
    stack = [[y, x]]
    while len(stack) > 0:
        [y, x] = stack[-1]
        stack.pop()
        if result[y][x] == old:
            result[y][x] = new
            if y + 1 < rows: stack.append([y + 1, x])
            if y - 1 >= 0: stack.append([y - 1, x])
            if x + 1 < cols: stack.append([y, x + 1])
            if x - 1 >= 0: stack.append([y, x - 1])
    return result