def read_input():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        left = []
        right = []
        for line in lines:
            left.append(line[:5])
            right.append(line[8:13])
        left = list(map(int, left))
        right = list(map(int, right))
        return sorted(left), sorted(right)


def get_distances(left, right):
    distances = []
    for i in range(len(left)):
        if right[i] > left[i]:
            distances.append(right[i] - left[i])
        else:
            distances.append(left[i] - right[i])
    return distances


def get_appearances(left, right):
    return [(element, right.count(element)) for element in left]


def get_similarity_score(appearances):
    return sum((appearance[0] * appearance[1]) for appearance in appearances)


l, r = read_input()
d = get_distances(l, r)
first_answer = sum(d)
a = get_appearances(l, r)
second_answer = get_similarity_score(a)
