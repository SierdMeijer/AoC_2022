
with open('Day1/input.txt', 'rt') as f:
    lines = f.readlines()
    
calories = []
elf = []
for line in lines:
    if line == '\n':
        calories.append(elf)
        elf = []
    else:
        elf.append(int(line.strip()))

# Add last elf
calories.append(elf)

def part1():

    highest = -1
    for elf in calories:
        val = sum(elf)
        if val > highest:
            highest = val

    return highest

def part2():
    def cal_sort(e):
        return sum(e)

    calories.sort(key=cal_sort, reverse=True)
    return sum([val for elf in calories[:3] for val in elf])


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")