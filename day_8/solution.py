from itertools import combinations


def read_input():
    clean_lines = []
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    for line in range(len(lines)):
        if line == len(lines) - 1:
            clean_lines.append(lines[line])
        else:
            clean_lines.append(lines[line][:-1])
    return clean_lines


def find_antennas(lines):
    antennas = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != '.':
                antennas.append((lines[i][j], i, j))
    return antennas, len(lines), len(lines[0])


def sort_antennas(antennas):
    sorted_antennas = []
    signs = []
    for antenna in antennas:
        if antenna[0] not in signs:
            signs.append(antenna[0])
    for sign in signs:
        sing_antennas = []
        for antenna in antennas:
            if antenna[0] == sign:
                sing_antennas.append(antenna)
        sorted_antennas.append(sing_antennas)
    return sorted_antennas


def combine_antennas(antennas):
    pairs = []
    for antenna in antennas:
        pairs.extend(list(combinations(antenna, 2))[:])
    return pairs


def find_antinodes(combined, height, width):
    antinodes = []
    for combination in combined:
        y_diff = combination[1][1] - combination[0][1]
        if combination[0][1] < combination[1][1] and combination[0][2] > combination[1][2]:
            x_diff = abs(combination[1][2] - combination[0][2])
            potential_first_node = (combination[0][1] - y_diff, combination[0][2] + x_diff)
            potential_second_node = (combination[1][1] + y_diff, combination[1][2] - x_diff)
            if 0 <= potential_first_node[0] < height and 0 <= potential_first_node[1] < width:
                antinodes.append(potential_first_node)
            if 0 <= potential_second_node[0] < height and 0 <= potential_second_node[1] < width:
                antinodes.append(potential_second_node)
        elif combination[0][1] < combination[1][1] and combination[0][2] < combination[1][2]:
            x_diff = combination[1][2] - combination[0][2]
            potential_first_node = (combination[0][1] - y_diff, combination[0][2] - x_diff)
            potential_second_node = (combination[1][1] + y_diff, combination[1][2] + x_diff)
            if 0 <= potential_first_node[0] < height and 0 <= potential_first_node[1] < width:
                antinodes.append(potential_first_node)
            if 0 <= potential_second_node[0] < height and 0 <= potential_second_node[1] < width:
                antinodes.append(potential_second_node)
    return set(antinodes)


def get_more_antinodes(antennas, height, width):
    antinodes = set()
    for antenna in antennas:
        coordinates = []
        for antenna_coordinates in antenna:
            coordinates.append((antenna_coordinates[1], antenna_coordinates[2]))
        for first_coordinate in coordinates:
            for second_coordinate in coordinates:
                if first_coordinate == second_coordinate:
                    continue
                y_diff = first_coordinate[0] - second_coordinate[0]
                x_diff = first_coordinate[1] - second_coordinate[1]
                point_y = second_coordinate[0]
                point_x = second_coordinate[1]
                while 0 <= point_y < height and 0 <= point_x < width:
                    antinodes.add((point_y, point_x))
                    point_y -= y_diff
                    point_x -= x_diff
    return antinodes


cl = read_input()
a, h, w = find_antennas(cl)
sa = sort_antennas(a)
p = combine_antennas(sa)
anti = find_antinodes(p, h, w)
first_answer = len(anti)
print(first_answer)
second_answer = len(get_more_antinodes(sa, h, w))
print(second_answer)