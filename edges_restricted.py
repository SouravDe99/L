import csv

edges = []


def mirror(grid):
    new_grid = [grid[3], grid[2], grid[1], grid[0]]
    return new_grid


def rotate(grid):
    new_grid = mirror(grid)
    new_new_grid = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    for p in range(0, 4):
        for q in range(0, 4):
            new_new_grid[p][q] = new_grid[q][p]
    return new_new_grid


def check(vertex1, vertex2, colour1, colour2):
    result = True
    c1_counter = 0
    neutral_counter = 0
    for p in range(0, 4):
        for q in range(0, 4):
            if (vertex1[p][q] == colour1) and (vertex2[p][q] == colour1):
                c1_counter += 1
            if (vertex1[p][q] == 'n') and (vertex2[p][q] == colour1):
                result = False
            if (vertex1[p][q] == colour2) and (vertex2[p][q] != colour2):
                result = False
            if (vertex1[p][q] == 'n') and (vertex2[p][q] != 'n'):
                neutral_counter += 1
    if neutral_counter >= 2:
        result = False
    if c1_counter >= 4:
        result = False
    return result


def check_blue(vertex1, vertex2):
    return check(vertex1, vertex2, 'b', 'r')


def check_red(vertex1, vertex2):
    result = False
    orientations = [vertex2, rotate(vertex2), rotate(rotate(vertex2)), rotate(rotate(rotate(vertex2))), mirror(vertex2),
                    rotate(mirror(vertex2)), rotate(rotate(mirror(vertex2))), rotate(rotate(rotate(mirror(vertex2))))]
    for vertex in orientations:
        if check(vertex1, vertex, 'r', 'b'):
            result = True
    return result


# main

file = open("vertices_restricted.txt", "r")
vertices = eval(file.read())
file.close()

for i in range(0, len(vertices)):
    temp = []
    for j in range(0, len(vertices)):
        temp.append('')
    edges.append(temp)

count = 1

for i in range(0, len(vertices)):
    for j in range(0, len(vertices)):
        if check_red(vertices[i], vertices[j]):
            edges[i][j] += 'r'
        if check_blue(vertices[i], vertices[j]):
            edges[i][j] += 'b'
    print(count)
    count += 1

file = open("edges_restricted.csv", "w", newline='\n')
writer = csv.writer(file)
writer.writerows(edges)
file.close()
