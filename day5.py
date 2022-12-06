from collections import deque

def get_crates():
    crates_file = open('advent5.txt', 'r')
    file_string = crates_file.read().split('\n\n')
    crates_string = file_string[0]
    crates_list = crates_string.split('\n')
    crates_list.pop()
    raw_crates_grid = [c.split(' ') for c in crates_list]
    new_crates_grid = []
    for crates_row in raw_crates_grid:
        new_crate_row = []
        i = 0
        while i < len(crates_row):
            if crates_row[i] == '':
                new_crate_row.append('[0]')
                i += 4
            else:
                new_crate_row.append(crates_row[i])
                i += 1
        new_crates_grid.append(new_crate_row)
    transposed_crates = []
    for i in range(len(new_crates_grid[0])):
        row = []
        for c in reversed(new_crates_grid):
            if c[i] != '[0]':
                row.append(c[i][1])
        transposed_crates.append(deque(row))
    return transposed_crates

def get_instructions():
    crates_file = open('advent5.txt', 'r')
    file_string = crates_file.read().split('\n\n')
    instructions_string = file_string[1]
    instructions_list = instructions_string.split('\n')
    numerical_instructions  = [[int(s) for s in txt.split() if s.isdigit()] for txt in instructions_list]
    return numerical_instructions

def execute_instructions_part1():
    crates_grid = get_crates()
    crates_dict = {}
    i = 1
    for crate in crates_grid:
        crates_dict[i] = crate
        i += 1
    instructions = get_instructions()
    for ins in instructions:
        num_crates = ins[0]
        source = ins[1]
        dest = ins[2]
        for _ in range(num_crates):
            c = crates_dict[source].pop()
            crates_dict[dest].append(c)
    final_crates = ''
    for j in crates_dict:
        final_crates += crates_dict[j].pop()
    return final_crates

def execute_instructions_part2():
    crates_grid = get_crates()
    crates_dict = {}
    i = 1
    for crate in crates_grid:
        crates_dict[i] = crate
        i += 1
    instructions = get_instructions()
    for ins in instructions:
        num_crates = ins[0]
        source = ins[1]
        dest = ins[2]
        temp_stack = []
        for _ in range(num_crates):
            c = crates_dict[source].pop()
            temp_stack.append(c)
        for t in reversed(temp_stack):
            crates_dict[dest].append(t)        
    final_crates = ''
    for j in crates_dict:
        final_crates += crates_dict[j].pop()
    return final_crates
    
            


if __name__=="__main__":
    print("Final crates on top for part 1 are: ", execute_instructions_part1())
    print("Final crates on top for part 2 are: ", execute_instructions_part2())

    