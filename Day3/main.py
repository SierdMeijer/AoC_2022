from string import ascii_lowercase, ascii_uppercase

priorities = {}
for i, (ll, lu) in enumerate(zip(ascii_lowercase, ascii_uppercase)):
    priorities[ll] = i+1
    priorities[lu] = i+27

lines = open('Day3/input.txt', 'rt').readlines()

def part1():
    score = 0
    for l in lines:
        p1 = set(l[:len(l)//2].strip())
        p2 = set(l[len(l)//2:].strip())

        score += priorities[[p for p in p1 if p in p2][0]]

    return score

def part2():
    score = 0
    for i in range(0, len(lines), 3):
        score += priorities[[p for p in set(lines[i].strip()) if p in set(lines[i+1].strip()) and p in set(lines[i+2].strip())][0]]

    return score


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")