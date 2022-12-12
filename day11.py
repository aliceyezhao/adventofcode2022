class Test:
    def __init__(self, divisible_by, t, f):
        self.divisible_by = divisible_by
        self.t = t
        self.f = f
        
class Monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0

def get_monkeys():
    monkey_raw = open('advent11.txt', 'r').read()
    monkey_blurbs = monkey_raw.split('\n\n')
    monkeys = {}
    for i in range(len(monkey_blurbs)):
        lines = monkey_blurbs[i].split('\n')

        divisible_by = int(lines[3].split()[-1])
        t = int(lines[4].split()[-1])
        f = int(lines[5].split()[-1])
        test = Test(divisible_by, t, f)
    
        items_raw = lines[1].replace('Starting items: ', '').split(', ')
        items = [int(item) for item in items_raw]

        op = lines[2].replace('Operation: new = ', '').strip()
        operation = get_operation(op) 

        monkeys[i] = Monkey(items, operation, test)
    return monkeys

def get_operation(op):
    return lambda old : eval(op)

def play_rounds(num_rounds, part1):
    monkeys = get_monkeys()
    common_divisor = 1
    for m in monkeys:
        common_divisor *= monkeys[m].test.divisible_by
        
    for _ in range(num_rounds):
        for i in range(len(monkeys)):
            for item in monkeys[i].items:
                monkeys[i].inspections += 1
                operation = monkeys[i].operation
                worry = operation(item)
                if part1:
                    worry //= 3
        
                case_t = worry % monkeys[i].test.divisible_by == 0
                if case_t:
                    if part1:
                        monkeys[monkeys[i].test.t].items.append(worry)
                    else:
                        monkeys[monkeys[i].test.t].items.append(worry % common_divisor)

                else:
                    if part1:
                        monkeys[monkeys[i].test.f].items.append(worry)
                    else:
                        monkeys[monkeys[i].test.f].items.append(worry % common_divisor)
                monkeys[i].items = []

    monkey_inspections = {}
    for m in monkeys:
        monkey_inspections[m] = monkeys[m].inspections

    monkey1 = max(monkey_inspections, key=monkey_inspections.get)
    val1 = monkey_inspections[monkey1]
    monkey_inspections[monkey1] = -1
    monkey2 = max(monkey_inspections, key=monkey_inspections.get)
    val2 = monkey_inspections[monkey2]
    return val1 * val2

if __name__ == "__main__":
    print("Monkey business for part one: ", play_rounds(20, True))
    print("Monkey business for part two: ", play_rounds(10000, False))

