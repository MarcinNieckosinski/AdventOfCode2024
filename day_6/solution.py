def read_input():
    clean_lines = []
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    for line in range(len(lines)):
        if line == len(lines) - 1:
            clean_lines.append(list(lines[line]))
        else:
            clean_lines.append(list(lines[line][:-1]))
    return clean_lines


def create_path(tilesets):
    pos_x = 0
    pos_y = 0
    direction = "up"
    height = len(tilesets) - 1
    width = len(tilesets[0]) - 1
    used_tiles = []
    for i in range(len(tilesets)):
        if '^' in tilesets[i]:
            pos_x = tilesets[i].index('^')
            pos_y = i
    while 0 < pos_x < width and 0 <= pos_y < height:
        if direction == "up":
            if tilesets[pos_y - 1][pos_x] != '#':
                pos_y -= 1
            else:
                direction = "right"
        elif direction == "right":
            if tilesets[pos_y][pos_x + 1] != '#':
                pos_x += 1
            else:
                direction = "down"
        elif direction == "down":
            if tilesets[pos_y + 1][pos_x] != '#':
                pos_y += 1
            else:
                direction = "left"
        elif direction == "left":
            if tilesets[pos_y][pos_x - 1] != '#':
                pos_x -= 1
            else:
                direction = "up"
        if (pos_y, pos_x) not in used_tiles:
            used_tiles.append((pos_y, pos_x))
    if pos_x == 0 or pos_y == 0:
        used_tiles.append((pos_y, pos_x))
    return used_tiles


def create_path_with_obstacles(tilesets, usedtiles):
    loopcount = 0
    pos_x = 0
    pos_y = 0
    height = len(tilesets) - 1
    width = len(tilesets[0]) - 1
    all_visited = []

    for i in range(len(tilesets)):
        if '^' in tilesets[i]:
            pos_x = tilesets[i].index('^')
            pos_y = i
    startpos = (pos_y, pos_x)
    for usedtile in usedtiles:
        if usedtile[0] == startpos[0] and usedtile[1] == startpos[1]:
            usedtiles.remove(usedtile)

    for index, usedtile in enumerate(usedtiles):
        visited = []
        direction = "up"
        for i in range(len(tilesets)):
            if '^' in tilesets[i]:
                pos_x = tilesets[i].index('^')
                pos_y = i

        tilesets[usedtile[0]][usedtile[1]] = '#'

        while 0 < pos_x < width and 0 < pos_y < height:
            if direction == "up":
                if tilesets[pos_y - 1][pos_x] != '#':
                    pos_y -= 1
                else:
                    if (pos_y - 1, pos_x, "down") in visited:
                        all_visited.append(tuple(visited))
                        loopcount += 1
                        break
                    else:
                        visited.append((pos_y - 1, pos_x, "down"))
                        direction = "right"
            elif direction == "right":
                if tilesets[pos_y][pos_x + 1] != '#':
                    pos_x += 1
                else:
                    if (pos_y, pos_x + 1, "left") in visited:
                        all_visited.append(tuple(visited))
                        loopcount += 1
                        break
                    else:
                        visited.append((pos_y, pos_x + 1, "left"))
                        direction = "down"
            elif direction == "down":
                if tilesets[pos_y + 1][pos_x] != '#':
                    pos_y += 1
                else:
                    if (pos_y + 1, pos_x, "up") in visited:
                        all_visited.append(tuple(visited))
                        loopcount += 1
                        break
                    else:
                        visited.append((pos_y + 1, pos_x, "up"))
                        direction = "left"
            elif direction == "left":
                if tilesets[pos_y][pos_x - 1] != '#':
                    pos_x -= 1
                else:
                    if (pos_y, pos_x - 1, "right") in visited:
                        all_visited.append(tuple(visited))
                        loopcount += 1
                        break
                    else:
                        visited.append((pos_y, pos_x - 1, "right"))
                        direction = "up"
        tilesets[usedtile[0]][usedtile[1]] = "."
    return loopcount - 1


cl = read_input()
ut = create_path(cl)
first_answer = len(ut)
second_answer = create_path_with_obstacles(cl, ut)