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

# blue_wins

for vertex in range(0, len(edges)):
    if vertex_degrees[vertex]['out_degree_red'] == 0:
        red_moves_blue_wins.add(vertex)

print("red_moves_blue_wins:", len(red_moves_blue_wins))

length = len(red_moves_blue_wins)
length_temp = 0

while length != length_temp:
    length_temp = length

    for vertex in range(0, len(edges)):
        for next_vertex in red_moves_blue_wins:
            if 'b' in edges[vertex][next_vertex]:
                blue_moves_blue_wins.add(vertex)

    print("blue_moves_blue_wins:", len(blue_moves_blue_wins))

    for vertex in range(0, len(edges)):
        counter = 0
        for next_vertex in blue_moves_blue_wins:
            if 'r' in edges[vertex][next_vertex]:
                counter += 1
        if counter == vertex_degrees[vertex]['out_degree_red']:
            red_moves_blue_wins.add(vertex)

    print("red_moves_blue_wins:", len(red_moves_blue_wins))
    length = len(red_moves_blue_wins)

print()

# red_wins

for vertex in range(0, len(edges)):
    if vertex_degrees[vertex]['out_degree_blue'] == 0:
        blue_moves_red_wins.add(vertex)

print("blue_moves_red_wins:", len(blue_moves_red_wins))

length = len(blue_moves_red_wins)
length_temp = 0

while length_temp != length:
    length_temp = length

    for vertex in range(0, len(edges)):
        for next_vertex in blue_moves_red_wins:
            if 'r' in edges[vertex][next_vertex]:
                red_moves_red_wins.add(vertex)

    print("red_moves_red_wins:", len(red_moves_red_wins))

    for vertex in range(0, len(edges)):
        counter = 0
        for next_vertex in red_moves_red_wins:
            if 'b' in edges[vertex][next_vertex]:
                counter += 1
        if counter == vertex_degrees[vertex]['out_degree_blue']:
            blue_moves_red_wins.add(vertex)

    length = len(blue_moves_red_wins)
    print("blue_moves_red_wins:", len(blue_moves_red_wins))

print()

# infinite_draw

red_moves_infinite_draw = set()
blue_moves_infinite_draw = set()

for vertex in range(0, len(edges)):
    red_moves_infinite_draw.add(vertex)
    blue_moves_infinite_draw.add(vertex)

red_moves_infinite_draw = red_moves_infinite_draw - red_moves_red_wins
red_moves_infinite_draw = red_moves_infinite_draw - red_moves_blue_wins
blue_moves_infinite_draw = blue_moves_infinite_draw - blue_moves_red_wins
blue_moves_infinite_draw = blue_moves_infinite_draw - blue_moves_blue_wins

temp = {'blue_positive': red_moves_red_wins, 'blue_negative': red_moves_blue_wins, 'blue_zero': red_moves_infinite_draw,
        'red_positive': blue_moves_red_wins, 'red_negative': blue_moves_blue_wins, 'red_zero': blue_moves_infinite_draw}

file = open("final_set.txt", "w")
file.write(str(temp))
file.close()
