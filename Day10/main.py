import numpy as np

def get_lines():
    return [line.strip().split() for line in open('Day10/input.txt', 'rt').readlines()]


def part1():
    lines = get_lines()
    busy = False
    X = 1
    tba = None
    score = 0

    for i in range(0, 221):
        if (i - 20) % 40 == 0:
            score += X * i

        if busy:
            busy = False
            continue

        if tba:
            X += tba
            tba = None

        instruction = lines.pop(0)
        if instruction[0] == 'noop':
            continue

        tba = int(instruction[1])
        busy = True
        
    return score

def part2():
    display = np.full([6, 40], '.')
    
    lines = get_lines()
    busy = False
    X = 1
    tba = None
    score = 0

    for i in range(0, 241):
        if (i - 20) % 40 == 0:
            score += X * i

        if busy:
            busy = False

        else:
            if tba:
                X += tba
                tba = None

            if len(lines) == 0:
                break

            instruction = lines.pop(0)
            if instruction[0] != 'noop':
                tba = int(instruction[1])
                busy = True

        disp_loc = (i // 40, i % 40)
        if X-1 <= disp_loc[1] <= X+1:
            display[disp_loc] = '#'

    for d in display:
        print(''.join(d.tolist()))

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")