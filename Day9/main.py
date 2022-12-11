lines = [line.strip().split() for line in open('Day9/input.txt', 'rt').readlines()]


def position_tail(h, t):

    if abs(h[0] - t[0]) < 2 and abs(h[1] - t[1]) < 2:
        return t

    if t[0] < h[0]:
        t[0] += 1
    elif t[0] > h[0]:
        t[0] -= 1
    
    if t[1] < h[1]:
        t[1] += 1
    elif t[1] > h[1]:
        t[1] -= 1

    return t


def part1():

    H = [0, 0]
    T = [0, 0]
    passed = []

    for line in lines:

        for _ in range(int(line[1])):

            match line[0]:

                case 'R':
                    H[0] += 1

                case 'L':
                    H[0] -= 1

                case 'U':
                    H[1] += 1

                case 'D':
                    H[1] -= 1

            T = position_tail(H, T)

            if T not in passed:
                passed.append([T[0], T[1]])

    return len(passed)

def part2():
    knots = [[0, 0] for _ in range(10)]
    passed = []

    for line in lines:

        for _ in range(int(line[1])):

            match line[0]:

                case 'R':
                    knots[0][0] += 1

                case 'L':
                    knots[0][0] -= 1

                case 'U':
                    knots[0][1] += 1

                case 'D':
                    knots[0][1] -= 1

            for i in range(1, len(knots)):
                knots[i] = position_tail(knots[i-1], knots[i])

            if knots[-1] not in passed:
                passed.append([knots[-1][0], knots[-1][1]])

    return len(passed)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")