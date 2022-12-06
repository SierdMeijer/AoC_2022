import copy

lines = open('Day5/input.txt', 'rt').readlines()

crates = [line.strip('\n') for line in lines[:lines.index('\n')-1]]
moves = [line.strip('\n') for line in lines[lines.index('\n')+1:]]
num_crates = len(lines[lines.index('\n')-1].split())

stacks = []
for i in range(num_crates):
    stacks.append([])
    for c in crates:
        add = c[i*4:i*4+3]
        if add != '   ':
            stacks[i].append(c[i*4:i*4+3])

    stacks[i].reverse()

def get_stacks():
    return copy.deepcopy(stacks)

moves = [[int(move.split()[i]) for i in [1, 3, 5]] for move in moves]

def part1():
    stacks = get_stacks()
    for move in moves:
        for _ in range(move[0]):
            stacks[move[2]-1].append(stacks[move[1]-1].pop())

    return ''.join([s[-1][1] for s in stacks])

def part2():   
    stacks = get_stacks()
    for move in moves:
        stacks[move[2]-1].extend(stacks[move[1]-1][-move[0]:])
        stacks[move[1]-1] = stacks[move[1]-1][:-move[0]]
        
    return ''.join([s[-1][1] for s in stacks])

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")