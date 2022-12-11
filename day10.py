def get_signal_strength():
    steps_raw = open('advent10.txt', 'r').readlines()
    steps = [step.replace('\n', '').split() for step in steps_raw]
    x = 1
    cycle = 0
    signal_cycles = [20, 60, 100, 140, 180, 220]
    to_sum = []

    for step in steps:
        if len(step) == 1:
            cycle += 1
            if cycle in signal_cycles:
                to_sum.append(x * cycle)
                signal_cycles.remove(cycle)
        else:
            v = int(step[1])
            cycle_range = set([cycle, cycle + 1, cycle + 2])
            relevant_cycles = cycle_range.intersection(signal_cycles)
            if len(relevant_cycles) > 0:
                c = relevant_cycles.pop()
                to_sum.append(x * c)
                signal_cycles.remove(c)
            x += v
            cycle += 2
    return(sum(to_sum))

def get_sprite(x):
    if x == -1:
        sprite = '#' * 1 + '.' * 39
    elif x == 0:
        sprite = '#' * 2 + '.' * 38
    elif x == 39:
        sprite = '.' * 38 + '#' * 2
    elif x == 40:
        sprite = '.' * 39 + '#' * 1
    elif x > 0 and x < 39:
        sprite = '.' * (x - 1) + '#' * 3 + '.' * (40 - 3 - x + 1)

    return sprite


def draw_sprite():
    steps_raw = open('advent10.txt', 'r').readlines()
    steps = [step.replace('\n', '').split() for step in steps_raw]
    x = 1
    cycle = 0
    sprite = get_sprite(x)
    row = ''
    for step in steps:
        # print(row)
        if len(step) == 1:
            if sprite[cycle] == '#':
                    row += '#'
            else:
                row += '.'
            if cycle == 39:
                print(row)
                row = ''
                cycle = 0
            else:
                cycle += 1
        else:
            v = int(step[1])
            if cycle == 39:
                if sprite[cycle] == '#':
                    row += '#'
                else:
                    row += '.'
                print(row)
                row = ''
                cycle = 0
                if sprite[cycle] == '#':
                    row += '#'
                else:
                    row += '.'
                cycle += 1
            else:  
                cycle_range = [cycle, cycle + 1]
                for c in cycle_range:
                    if sprite[c] == '#':
                        row += '#'
                    else:
                        row += '.'
                cycle += 2
            x += v
            sprite = get_sprite(x)

        if cycle == 40:
            print(row)
            row = ''
            cycle = 0

if __name__ == "__main__":
    print("The sum of signal strengths is: ", get_signal_strength())
    draw_sprite()
