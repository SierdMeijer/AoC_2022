with open('Day2/input.txt', 'rt') as f:
    lines = f.readlines()

rounds = [line.split() for line in lines]

points = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3,
    'win': 6,
    'draw': 3,
    'loss': 0,
}

def part1():
    def beat_it(a, b):
        #      R    P    S
        c1 = ['A', 'B', 'C']
        c2 = ['X', 'Y', 'Z']

        val = c1.index(a) - c2.index(b)
        if val == 0:
            return 'draw'
        elif val == 1 or val == -2:
            return 'loss'
        else:
            return 'win'

    score = 0
    for r in rounds:
        score += points[r[1]] + points[beat_it(r[0], r[1])]

    return score

def part2():
    def beat_it(a, b):
        #      R    P    S
        c1 = ['A', 'B', 'C']
        #      L    D    W
        c2 = ['X', 'Y', 'Z']

        match c2.index(b):
            case 0:
                return c1[c1.index(a) - 1 if c1.index(a) - 1 >= 0 else 2], 0
            case 1:
                return c1[c1.index(a)], 1
            case 2:
                return c1[c1.index(a) + 1 if c1.index(a) + 1 <= 2 else 0], 2

    score = 0
    for r in rounds:
        me, outcome = beat_it(r[0], r[1])
        score += points[me] + (outcome * 3)

    return score
    

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")