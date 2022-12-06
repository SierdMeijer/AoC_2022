lines = [line.strip() for line in open('Day6/input.txt', 'rt').readlines()]

def part1():
    for line in lines:
        for i in range(len(line)):
            if len(set(line[i:i+4])) == 4:
                print(f'Found begin at {i+4}')
                break

def part2():   
    for line in lines:
        for i in range(len(line)):
            if len(set(line[i:i+14])) == 14:
                print(f'Found begin at {i+14}')
                break

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")