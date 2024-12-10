def read_input():
    with open('input.txt', 'r') as file:
        return file.readline()


def get_files(instruction):
    files = []
    id_ = 0
    for i in range(len(instruction)):
        if i % 2 == 0:
            files.extend([id_] * int(instruction[i]))
            id_ += 1
        else:
            files.extend(['.'] * int(instruction[i]))
    return files


def move_in_singles(files):
    counted_space = files.count('.')
    moved_files = []
    counter = -1
    for i in range(len(files)):
        if len(moved_files) < len(files) - counted_space:
            if files[i] != '.':
                moved_files.append(files[i])
            elif files[counter] == '.':
                while files[counter] == '.':
                    counter -= 1
                moved_files.append(files[counter])
                counter -= 1
            else:
                moved_files.append(files[counter])
                counter -= 1
    return moved_files



def count_checksum(files):
    checksum = 0
    for index, file in enumerate(files):
        if file != '.':
            checksum += index * int(file)
    return checksum


def move_in_batches(instruction):
    files = []
    moved_files = []
    id_ = 0
    for i in range(len(instruction)):
        if i % 2 == 0:
            files.append((int(instruction[i]), str(id_)))
            id_ += 1
        else:
            files.append((int(instruction[i]), '.'))
    for i in reversed(range(len(files))):
        for j in range(i):
            i_block_size, i_block_data = files[i]
            j_block_size, j_block_data = files[j]
            if i_block_data != '.' and j_block_data == '.' and i_block_size <= j_block_size:
                files[i] = (i_block_size, '.')
                files[j] = (j_block_size - i_block_size, '.')
                files.insert(j, (i_block_size, i_block_data))
    for i in files:
        for j in range(i[0]):
            moved_files.append(i[1])
    return moved_files

ins = read_input()
f = get_files(ins)
mf = move_in_singles(f)
first_answer = count_checksum(mf)
mf = move_in_batches(ins)
second_answer = count_checksum(mf)
