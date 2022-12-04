
lines = open('Day4/input.txt', 'rt').readlines()

pairs = [[[int(val) for val in ids.split('-')] for ids in line.strip().split(',')] for line in lines]

def part1():
    count = 0
    for pair in pairs:
        p1, p2 = pair[0], pair[1]

        if (p1[0] <= p2[0] and p1[1] >= p2[1]) or \
            (p1[0] >= p2[0] and p1[1] <= p2[1]):

            count += 1

    return count

def part2():   
    count = 0
    for pair in pairs:
        p1, p2 = pair[0], pair[1]

        if p1[0] <= p2[0] <= p1[1] or \
           p1[0] <= p2[1] <= p1[1] or \
           p2[0] <= p1[0] <= p2[1] or \
           p2[0] <= p1[1] <= p2[1]:

            count += 1

    return count

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")