def read_input():
    clean_lines = []
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    for line in range(len(lines)):
        if line == len(lines) - 1:
            clean_lines.append(list(map(int, lines[line])))
        else:
            clean_lines.append(list(map(int, lines[line][:-1])))
    return clean_lines


def find_trailheads(topography):
    trailheads = []
    for i in range(len(topography)):
        for j in range(len(topography[0])):
            if topography[i][j] == 0:
                trailheads.append((i, j))
    return trailheads


def find_next_points(topography, points, searched, stop=False, no_repeats=False):
    next_points = []
    if searched + 1 <= 10:
        for p in points:
            if p[0] - 1 >= 0 and topography[p[0] - 1][p[1]] == searched:
                next_points.append((p[0] - 1, p[1]))
            if p[1] + 1 < len(topography[0]) and topography[p[0]][p[1] + 1] == searched:
                next_points.append((p[0], p[1] + 1))
            if p[0] + 1 < len(topography) and topography[p[0] + 1][p[1]] == searched:
                next_points.append((p[0] + 1, p[1]))
            if p[1] - 1 >= 0 and topography[p[0]][p[1] - 1] == searched:
                next_points.append((p[0], p[1] - 1))
        searched += 1
        searched, next_points, stop = find_next_points(topography, next_points, searched, stop, no_repeats)
    else:
        stop = True
        next_points = points
    if no_repeats:
        next_points = set(next_points)
    return searched, next_points, stop


def find_finals(topography, trailheads, no_repeats=False):
    finals = 0
    for th in trailheads:
        stop = False
        start = [th]
        searching = 1
        while not stop:
            searching, start, stop = find_next_points(topography, start, searching, stop, no_repeats)
        finals += len(start)
    return finals



cl = read_input()
t = find_trailheads(cl)
first_answer = find_finals(cl, t, True)
print(first_answer)
second_answer = find_finals(cl, t, False)
print(second_answer)
