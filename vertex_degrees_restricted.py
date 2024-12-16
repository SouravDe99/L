import csv

# main

edges = []
vertex_degrees = []

file = open("edges_restricted.csv", "r")
reader = csv.reader(file)
for row in reader:
    edges.append(row)
file.close()

for i in range(0, len(edges)):
    vertex_degrees.append({'in_degree_red': 0, 'in_degree_blue': 0, 'out_degree_red': 0, 'out_degree_blue': 0})

for i in range(0, len(edges)):
    for j in range(0, len(edges)):
        if 'r' in edges[i][j]:
            vertex_degrees[j]['in_degree_red'] += 1
            vertex_degrees[i]['out_degree_red'] += 1
        if 'b' in edges[i][j]:
            vertex_degrees[j]['in_degree_blue'] += 1
            vertex_degrees[i]['out_degree_blue'] += 1

file = open("vertex_degrees_restricted.txt", "w")
file.write(str(vertex_degrees))
file.close()
