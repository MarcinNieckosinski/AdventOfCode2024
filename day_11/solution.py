from functools import cache


def read_input():
    with open('input.txt', 'r') as file:
        inp = []
        line = file.readline().split(' ')
        for l in line:
            inp.append(int(l))
        return inp


def blink_for_stone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone = str(stone)
        middle = int(len(stone) // 2)
        return [int(stone[:middle]), int(stone[middle:])]
    else:
        return [stone * 2024]

@cache
def blink_many_times(stone, times):
    if times == 0:
        return 1
    return sum(blink_many_times(st, times - 1) for st in blink_for_stone(stone))



i = read_input()
first_answer = sum(blink_many_times(s, 25) for s in i)
second_answer = sum(blink_many_times(s, 75) for s in i)
