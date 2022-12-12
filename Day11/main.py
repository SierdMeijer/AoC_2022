
from copy import copy
from tqdm import tqdm

lines = [line.strip() for line in open('Day11/input.txt', 'rt').readlines()]

def get_monkeys():
    monkeys = []
    for i, line in enumerate(lines):

        match i % 7:
            case 0:
                monkeys.append({
                    'inspected': 0
                })

            case 1:
                monkeys[-1]['items'] = [val for val in line.split(':')[1].split(',')]

            case 2:
                monkeys[-1]['operation'] = line.split(':')[1].split('=')[1]

            case 3:
                monkeys[-1]['test'] = int(line.split()[-1])

            case 4:
                monkeys[-1]['true'] = int(line.split()[-1])
            
            case 5:
                monkeys[-1]['false'] = int(line.split()[-1])
        
    return monkeys


def part1():
    monkeys = get_monkeys()
    
    for _ in range(20):
        for monkey in monkeys:
            
            while len(monkey['items']) != 0:

                new = eval(copy(monkey['operation']).replace('old', str(monkey['items'].pop(0)))) // 3
                monkey['inspected'] += 1

                if new % monkey['test'] == 0:
                    monkeys[monkey['true']]['items'].append(new)
                else:
                    monkeys[monkey['false']]['items'].append(new)

    values = sorted([m['inspected'] for m in monkeys])
    print(values)

    return values[-1] * values[-2]


def part2():
    monkeys = get_monkeys()
    mod_factor = 1 
    for m in monkeys:
        mod_factor *= m['test']

    for _ in tqdm(range(10000)):
        for monkey in monkeys:
            
            while len(monkey['items']) != 0:

                new = eval(copy(monkey['operation']).replace('old', str(monkey['items'].pop(0))))
                monkey['inspected'] += 1

                if new % monkey['test'] == 0:
                    monkeys[monkey['true']]['items'].append(new % mod_factor)
                else:
                    monkeys[monkey['false']]['items'].append(new % mod_factor)

    values = sorted([m['inspected'] for m in monkeys])
    print(values)

    return values[-1] * values[-2]


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")