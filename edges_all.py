import csv

edges = []


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


# main

file = open("vertices_all.txt", "r")
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
        if check(vertices[i], vertices[j], 'r', 'b'):
            edges[i][j] += 'r'
        if check(vertices[i], vertices[j], 'b', 'r'):
            edges[i][j] += 'b'
    print(count)
    count += 1

file = open("edges_all.csv", "w", newline='\n')
writer = csv.writer(file)
writer.writerows(edges)
file.close()
