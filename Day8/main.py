import numpy as np

lines = np.array([[int(l) for l in line.strip()] for line in open('Day8/input.txt', 'rt').readlines()])

def part1():
    count = lines.shape[0] * 2 + lines.shape[1] * 2 - 4
    for i in range(1, lines.shape[0]-1):
        for j in range(1, lines.shape[1]-1):
            if lines[i, j] > max(lines[:i, j]) or \
               lines[i, j] > max(lines[i+1:, j]) or \
               lines[i, j] > max(lines[i, :j]) or \
               lines[i, j] > max(lines[i, j+1:]):
                
                count += 1

    return count

def part2():
    highscore = 0
    for i in range(1, lines.shape[0]-1):
        for j in range(1, lines.shape[1]-1):
            views = [0, 0, 0, 0]
            directions = [
                np.flip(lines[:i, j]),
                lines[i+1:, j],
                np.flip(lines[i, :j]),
                lines[i, j+1:]
            ]

            for k, d in enumerate(directions):
                for t in d:
                    if lines[i, j] > t:
                        views[k] += 1
                    else:
                        views[k] += 1
                        break

            score = np.prod(views)
            if score > highscore:
                highscore = score

    return highscore

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")