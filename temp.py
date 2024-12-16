print("Hello World")

file = open("vertices_restricted.txt", "r")
vertices = eval(file.read())
file.close()

i = 1686
print(vertices[i])
for j in range(0, 4):
    print(vertices[i][j])

"""
import csv

edges = []
red_moves_blue_wins = set()
blue_moves_blue_wins = set()
blue_moves_red_wins = set()
red_moves_red_wins = set()

file = open("edges_restricted.csv", "r")
reader = csv.reader(file)
for row in reader:
    edges.append(row)
file.close()

file = open("vertex_degrees_restricted.txt", "r")
vertex_degrees = eval(file.read())
file.close()

for vertex in range(0, len(edges)):
    if vertex_degrees[vertex]['out_degree_blue'] == 0:
        blue_moves_red_wins.add(vertex)

print("blue_moves_red_wins:", sorted(blue_moves_red_wins))

length = len(blue_moves_red_wins)
length_temp = 0

while length_temp != length:
    length_temp = length

    for vertex in range(0, len(edges)):
        for next_vertex in blue_moves_red_wins:
            if 'r' in edges[vertex][next_vertex]:
                red_moves_red_wins.add(vertex)

    for vertex in range(0, len(edges)):
        counter = 0
        for next_vertex in red_moves_red_wins:
            if 'b' in edges[vertex][next_vertex]:
                counter += 1
        if counter == vertex_degrees[vertex]['out_degree_blue']:
            blue_moves_red_wins.add(vertex)

    length = len(blue_moves_red_wins)
    print("blue_moves_red_wins:", sorted(blue_moves_red_wins))
"""