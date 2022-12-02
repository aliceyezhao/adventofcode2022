def food_rations():
    rations = open('advent1.txt', 'r')
    rations_str = rations.read()
    rations_list = rations_str.split('\n\n')
    rations_sublist = [list(r.split('\n')) for r in rations_list]
    rations_sum = [sum([int(r) for r in ration]) for ration in rations_sublist]
    return rations_sum

def part1():
    return max(food_rations())

def part2():
    rations = food_rations()
    max1 = max(rations)
    rations.remove(max1)
    max2 = max(rations)
    rations.remove(max2)
    max3 = max(rations)
    rations.remove(max3)
    return max1 + max2 + max3

if __name__=="__main__":
    print("Max rations is: ", part1())
    print("Top 3 rations together is: ", part2())


