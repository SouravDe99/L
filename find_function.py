import csv
import sys

sys.setrecursionlimit(20000)

edges = []
explored_red = {}
explored_blue = {}
second_appearances = {'blue_positive': set(), 'blue_negative': set(), 'blue_zero': set(), 'red_positive': set(),
                      'red_negative': set(), 'red_zero': set()}


def minimax(index, depth, player):
    global counter

    # base_case

    if player == 'r':
        if index in explored_blue.keys():
            if explored_blue[index] is None:
                if index in second_appearances['blue_positive']:
                    explored_blue[index] = 1
                elif index in second_appearances['blue_negative']:
                    explored_blue[index] = -1
                elif index in second_appearances['blue_zero']:
                    explored_blue[index] = 0
                else:
                    explored_blue[index] = 0
        else:
            if vertex_degrees[index]['out_degree_red'] == 0:
                explored_blue[index] = -1
                temp['blue_negative'].add(index)
            else:
                explored_blue[index] = None
        if explored_blue[index] is not None:
            return explored_blue[index]
    if player == 'b':
        if index in explored_red.keys():
            if explored_red[index] is None:
                if index in second_appearances['red_positive']:
                    explored_red[index] = 1
                elif index in second_appearances['red_negative']:
                    explored_red[index] = -1
                elif index in second_appearances['red_zero']:
                    explored_red[index] = 0
                else:
                    explored_red[index] = 0
        else:
            if vertex_degrees[index]['out_degree_blue'] == 0:
                explored_red[index] = 1
                temp['red_positive'].add(index)
            else:
                explored_red[index] = None
        if explored_red[index] is not None:
            return explored_red[index]

    # recursive case

    if player == 'r':
        max_value = -1
        for next_index in range(0, len(edges)):
            if 'r' in edges[index][next_index]:
                value = minimax(next_index, depth + 1, 'b')
                max_value = max(max_value, value)
        if explored_blue[index] is not None and explored_blue[index] != max_value:
            counter += 1
        explored_blue[index] = max_value
        if max_value == 1:
            temp['blue_positive'].add(index)
        if max_value == -1:
            temp['blue_negative'].add(index)
        if max_value == 0:
            temp['blue_zero'].add(index)
        return max_value

    if player == 'b':
        min_value = 1
        for next_index in range(0, len(edges)):
            if 'b' in edges[index][next_index]:
                value = minimax(next_index, depth + 1, 'r')
                min_value = min(min_value, value)
        if explored_red[index] is not None and explored_red[index] != min_value:
            counter += 1
        explored_red[index] = min_value
        if min_value == 1:
            temp['red_positive'].add(index)
        if min_value == -1:
            temp['red_negative'].add(index)
        if min_value == 0:
            temp['red_zero'].add(index)
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

counter = -1
while counter != 0:
    explored_red = {}
    explored_blue = {}
    counter = 0
    temp = {'blue_positive': set(), 'blue_negative': set(), 'blue_zero': set(), 'red_positive': set(),
            'red_negative': set(), 'red_zero': set()}
    minimax(1686, 0, 'r')
    second_appearances['blue_positive'] = second_appearances['blue_positive'].union(temp['blue_positive'])
    second_appearances['blue_positive'] = second_appearances['blue_positive'] - temp['blue_negative']
    second_appearances['blue_positive'] = second_appearances['blue_positive'] - temp['blue_zero']
    second_appearances['blue_negative'] = second_appearances['blue_negative'].union(temp['blue_negative'])
    second_appearances['blue_negative'] = second_appearances['blue_negative'] - temp['blue_positive']
    second_appearances['blue_negative'] = second_appearances['blue_negative'] - temp['blue_zero']
    second_appearances['blue_zero'] = second_appearances['blue_zero'].union(temp['blue_zero'])
    second_appearances['blue_zero'] = second_appearances['blue_zero'] - temp['blue_positive']
    second_appearances['blue_zero'] = second_appearances['blue_zero'] - temp['blue_negative']
    second_appearances['red_positive'] = second_appearances['red_positive'].union(temp['red_positive'])
    second_appearances['red_positive'] = second_appearances['red_positive'] - temp['red_negative']
    second_appearances['red_positive'] = second_appearances['red_positive'] - temp['red_zero']
    second_appearances['red_negative'] = second_appearances['red_negative'].union(temp['red_negative'])
    second_appearances['red_negative'] = second_appearances['red_negative'] - temp['red_positive']
    second_appearances['red_negative'] = second_appearances['red_negative'] - temp['red_zero']
    second_appearances['red_zero'] = second_appearances['red_zero'].union(temp['red_zero'])
    second_appearances['red_zero'] = second_appearances['red_zero'] - temp['red_positive']
    second_appearances['red_zero'] = second_appearances['red_zero'] - temp['red_negative']
    print(counter)

file = open("final_minimax.txt", "w")
file.write(str(second_appearances))
file.close()
