vertices_temp = []
vertices = []

pieces = [{'up': 2, 'right': 1, 'down': 0, 'left': 0}, {'up': 1, 'right': 0, 'down': 0, 'left': 2},
          {'up': 0, 'right': 0, 'down': 2, 'left': 1}, {'up': 0, 'right': 2, 'down': 1, 'left': 0},
          {'up': 2, 'right': 0, 'down': 0, 'left': 1}, {'up': 0, 'right': 0, 'down': 1, 'left': 2},
          {'up': 0, 'right': 1, 'down': 2, 'left': 0}, {'up': 1, 'right': 2, 'down': 0, 'left': 0}]


def copy(grid):
    new_grid = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    for x in range(0, 4):
        for y in range(0, 4):
            new_grid[x][y] = grid[x][y]
    return new_grid


def check(piece, x, y, grid):
    result = True
    if (x - piece['up'] < 0) or (y + piece['right'] > 3) or (x + piece['down'] > 3) or (y - piece['left'] < 0):
        result = False
    else:
        if grid[x][y] != ' ':
            result = False
        for k in range(1, piece['up'] + 1):
            if grid[x - k][y] != ' ':
                result = False
        for k in range(1, piece['right'] + 1):
            if grid[x][y + k] != ' ':
                result = False
        for k in range(1, piece['down'] + 1):
            if grid[x + k][y] != ' ':
                result = False
        for k in range(1, piece['left'] + 1):
            if grid[x][y - k] != ' ':
                result = False
    return result


def put(piece, x, y, grid, colour):
    grid[x][y] = colour
    for k in range(1, piece['up'] + 1):
        grid[x - k][y] = colour
    for k in range(1, piece['right'] + 1):
        grid[x][y + k] = colour
    for k in range(1, piece['down'] + 1):
        grid[x + k][y] = colour
    for k in range(1, piece['left'] + 1):
        grid[x][y - k] = colour


# main

for red_piece in pieces:
    for i in range(0, 4):
        for j in range(0, 4):
            board = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
            if check(red_piece, i, j, board):
                put(red_piece, i, j, board, 'r')
                for blue_piece in pieces:
                    for p in range(0, 4):
                        for q in range(0, 4):
                            new_board = copy(board)
                            if check(blue_piece, p, q, new_board):
                                put(blue_piece, p, q, new_board, 'b')
                                vertices_temp.append(new_board)

print(len(vertices_temp))

for vertex in vertices_temp:
    for i in range(0, 4):
        for j in range(0, 4):
            board = copy(vertex)
            if board[i][j] == ' ':
                board[i][j] = 'n'
                for q in range(j, 4):
                    new_board = copy(board)
                    if new_board[i][q] == ' ':
                        new_board[i][q] = 'n'
                        vertices.append(new_board)
                for p in range(i + 1, 4):
                    for q in range(0, 4):
                        new_board = copy(board)
                        if new_board[p][q] == ' ':
                            new_board[p][q] = 'n'
                            vertices.append(new_board)

print(len(vertices))

file = open("vertices_all.txt", "w")
file.write(str(vertices))
file.close()
