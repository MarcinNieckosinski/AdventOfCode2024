from itertools import product


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


def make_equation_pairs(lines):
    pairs = []
    for line in lines:
        pairs.append((int(line.split(': ')[0]), line.split(': ')[1], line.split(':')[1][1:].count(' ')))
    return pairs


def combine_signs(signs, length):
    return product(signs,repeat=length)


def concat(first_num, second_num):
    return str(first_num) + str(second_num)


def clean_pairs(pairs, good_results):
    clean = []
    for pair in pairs:
        if pair[0] not in good_results:
            clean.append(pair)
    return clean


def try_equations(signs, pairs):
    good_results = []
    for i, pair in enumerate(pairs):
        print(i, len(pairs))
        combinations = list(combine_signs(signs, pair[2]))
        for combination in combinations:
            equation = ''
            numbers = pair[1].split(' ')
            for index in range(len(numbers)):
                if index > 0:
                    equation += combination[index - 1]
                equation += numbers[index]
                if '||' in equation:
                    equation = equation.split('||')[0] + equation.split('||')[1]
                else:
                    equation = str(eval(equation))
            if int(equation) == pair[0]:
                good_results.append(pair[0])
    return set(good_results)

cl = read_input()
p = make_equation_pairs(cl)
gr = try_equations(['+', '*'], p)
first_answer = sum(gr)
cp = clean_pairs(p, gr)
gr = try_equations(['+', '*', '||'], cp)
second_answer = first_answer + sum(gr)