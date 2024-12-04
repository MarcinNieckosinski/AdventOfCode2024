import re


def read_input():
    # input should have one blank line at the end
    clean_lines = []
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        clean_lines.append(line[:-1])
    return clean_lines


def find_all_muls(line):
    muls = []
    pattern = re.compile(r'mul\([0-9]+,[0-9]+\)')
    found = re.findall(pattern, line)
    for mul in found:
        muls.append((int(mul[4:-1].split(',')[0]), int(mul[4:-1].split(',')[1])))
    return muls


def add_muls(muls):
    outcomes = []
    for mul in muls:
        outcomes.append(mul[0] * mul[1])
    return sum(outcomes)

def use_do_and_dont(line):
    clean_lines = []
    after_do = line.split('do()')
    for ad in after_do:
        clean_lines.append(ad.split('don\'t()')[0])
    return clean_lines


cl = read_input()
muls_in_line_sums = []
for l in cl:
    line_muls = find_all_muls(l)
    muls_in_line_sums.append(add_muls(line_muls))
first_answer = sum(muls_in_line_sums)
muls_after_do_and_dont = []
muls_in_line_sums = []
for l in cl:
    muls_after_do_and_dont.append(use_do_and_dont(l))
for m in muls_after_do_and_dont:
    for element in m:
        line_muls = find_all_muls(element)
        muls_in_line_sums.append(add_muls(line_muls))
second_answer = sum(muls_in_line_sums)
print(second_answer)
