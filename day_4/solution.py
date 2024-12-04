def read_input():
    # input should have one blank line at the end
    clean_lines = []
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        clean_lines.append(list(line[:-1]))
    return clean_lines


def count_xmas(lines):
    counter = 0
    matrix_length = len(lines[0])
    matrix_height = len(lines)
    for i in range(matrix_height):
        for j in range(matrix_length):
            if lines[i][j] == 'X':
                if j - 1 >= 0 and j - 2 >= 0 and j - 3 >= 0:
                    if lines[i][j - 1] == 'M' and lines[i][j - 2] == 'A' and lines[i][j - 3] == 'S':
                        counter += 1
                if j - 1 >= 0 and j - 2 >= 0 and j - 3 >= 0 and i - 1 >= 0 and i - 2 >= 0 and i - 3 >= 0:
                    if lines[i - 1][j - 1] == 'M' and lines[i - 2][j - 2] == 'A' and lines[i - 3][j - 3] == 'S':
                        counter += 1
                if i - 1 >= 0 and i - 2 >= 0 and i - 3 >= 0:
                    if lines[i - 1][j] == 'M' and lines[i - 2][j] == 'A' and lines[i - 3][j] == 'S':
                        counter += 1
                if (j + 1 < matrix_length and j + 2 < matrix_length and j + 3 < matrix_length and i - 1 >= 0 and
                        i - 2 >= 0 and i - 3 >= 0):
                    if lines[i - 1][j + 1] == 'M' and lines[i - 2][j + 2] == 'A' and lines[i - 3][j + 3] == 'S':
                        counter += 1
                if j + 1 < matrix_length and j + 2 < matrix_length and j + 3 < matrix_length:
                    if lines[i][j + 1] == 'M' and lines[i][j + 2] == 'A' and lines[i][j + 3] == 'S':
                        counter += 1
                if (j + 1 < matrix_length and j + 2 < matrix_length and j + 3 < matrix_length and
                        i + 1 < matrix_height and i + 2 < matrix_height and i + 3 < matrix_height):
                    if lines[i + 1][j + 1] == 'M' and lines[i + 2][j + 2] == 'A' and lines[i + 3][j + 3] == 'S':
                        counter += 1
                if i + 1 < matrix_height and i + 2 < matrix_height and i + 3 < matrix_height:
                    if lines[i + 1][j] == 'M' and lines[i + 2][j] == 'A' and lines[i + 3][j] == 'S':
                        counter += 1
                if (j - 1 >= 0 and j - 2 >= 0 and j - 3 >= 0 and i + 1 < matrix_height and
                        i + 2 < matrix_height and i + 3 < matrix_height):
                    if lines[i + 1][j - 1] == 'M' and lines[i + 2][j - 2] == 'A' and lines[i + 3][j - 3] == 'S':
                        counter += 1
    return counter


def count_mas(lines):
    counter = 0
    matrix_length = len(lines[0])
    matrix_height = len(lines)
    for i in range(matrix_height):
        for j in range(matrix_length):
            if lines[i][j] == 'A':
                if i - 1 >= 0 and i + 1 < matrix_height and j - 1 >= 0 and j + 1 < matrix_length:
                    if lines[i - 1][j - 1] == lines[i - 1][j + 1] == 'M' and lines[i + 1][j - 1] == lines[i + 1][
                        j + 1] == 'S':
                        counter += 1
                    if lines[i - 1][j + 1] == lines[i + 1][j + 1] == 'M' and lines[i - 1][j - 1] == lines[i + 1][
                        j - 1] == 'S':
                        counter += 1
                    if lines[i + 1][j - 1] == lines[i + 1][j + 1] == 'M' and lines[i - 1][j - 1] == lines[i - 1][
                        j + 1] == 'S':
                        counter += 1
                    if lines[i - 1][j - 1] == lines[i + 1][j - 1] == 'M' and lines[i - 1][j + 1] == lines[i + 1][
                        j + 1] == 'S':
                        counter += 1
    return counter


cl = read_input()
first_answer = count_xmas(cl)
second_answer = count_mas(cl)