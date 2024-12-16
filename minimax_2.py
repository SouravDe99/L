import csv
import sys

sys.setrecursionlimit(20000)

edges = []
explored = []
examined = []


def minimax(index, alpha, beta, depth, player):
    global counter
    print(depth)

    # base_case

    for i in range(0, len(examined)):
        if player == 'r' and examined[i][0] == index and examined[i][1] == 'b':
            return examined[i][2]
        if player == 'b' and examined[i][0] == index and examined[i][1] == 'r':
            return examined[i][2]
    for i in range(0, len(explored)):
        if player == 'r' and i % 2 == 0 and explored[i] == index:
            examined.append([index, 'b', 0])
            return 0
        if player == 'b' and i % 2 == 1 and explored[i] == index:
            examined.append([index, 'r', 0])
            return 0
    if player == 'r' and vertex_degrees[index]['out_degree_red'] == 0:
        examined.append([index, 'b', -1])
        return -1
    if player == 'b' and vertex_degrees[index]['out_degree_blue'] == 0:
        examined.append([index, 'r', 1])
        return 1
    explored.append(index)

    # recursive case

    if player == 'r':
        max_value = -2
        for next_index in range(0, len(edges)):
            if 'r' in edges[index][next_index]:
                value = minimax(next_index, alpha, beta, depth + 1, 'b')
                max_value = max(max_value, value)
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
        for i in range(0, len(examined)):
            if examined[i][0] == index and examined[i][1] == 'b':
                if examined[i][2] != max_value:
                    counter += 1
                examined[i][2] = max_value
        else:
            examined.append([index, 'b', max_value])
        explored.pop()
        return max_value

    if player == 'b':
        min_value = 2
        for next_index in range(0, len(edges)):
            if 'b' in edges[index][next_index]:
                value = minimax(next_index, alpha, beta, depth + 1, 'r')
                min_value = min(min_value, value)
                beta = min(beta, value)
                if beta <= alpha:
                    break
        for i in range(0, len(examined)):
            if examined[i][0] == index and examined[i][1] == 'r':
                if examined[i][2] != min_value:
                    counter += 1
                examined[i][2] = min_value
        else:
            examined.append([index, 'r', min_value])
        explored.pop()
        return min_value


# main

file = open("edges_restricted.csv", "r")
reader = csv.reader(file)
for row in reader:
    edges.append(row)
file.close()

file = open("vertex_degrees_restricted.txt", "r")
vertex_degrees = eval(file.read())
file.close()

counter = 0
vertex = 1686
first_player = 'r'
if first_player == 'b':
    explored.append(None)
print("Value: ", minimax(vertex, -1, 1, 0, first_player))
print("Number of disagreements: ", counter)
