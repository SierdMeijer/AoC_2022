lines = [line.strip().split() for line in open('Day7/input.txt', 'rt').readlines()]

sizes = {}
pwd = []
for line in lines:

    match line[0]:
        case '$':
            if line[1] == 'cd':
                if line[2] == '..':
                    pwd.pop()
                else:
                    pwd.append(line[2])
                    path = '/'.join(pwd) if len(pwd) == 1 else '/'.join(pwd)[1:]
                    if path not in sizes:
                        sizes[path] = 0
                
        case 'dir':
            continue

        case _:
            for i in range(1, len(pwd)+1):
                path = '/'.join(pwd[:i]) if i == 1 else '/'.join(pwd[:i])[1:]
                sizes[path] += int(line[0])


def part1():

    total = 0
    for size in sizes.values():
        if size <= 100000:
            total += size

    return total

def part2():
    total = 70000000
    req = 30000000
    used = sizes['/']
    free = total - used
    
    smallest = 999999999999999999
    for s in sizes.values():
        if free + s > req and s < smallest:
            smallest = s

    return smallest
    

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")