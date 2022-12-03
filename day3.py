def get_rucksacks():
    rucksack_file = open('advent3.txt', 'r')
    rucksack_raw = rucksack_file.read().splitlines()
    return rucksack_raw

def get_common_item_score():
    rucksack_raw = get_rucksacks()
    total_score = 0
    for rucksack in rucksack_raw:
        n = len(rucksack)
        first = rucksack[0:n//2]
        second = rucksack[n//2:n]
        common = [f for f in first if f in second]
        score = ord(common[0])
        if score >= 97:
            total_score += score - 96
        else:
            total_score += score - 38
    return total_score

def get_trio_common_item_score():
    rucksack_raw = get_rucksacks()
    total_score = 0
    i = 0
    while i < len(rucksack_raw) - 2:
        first = list(rucksack_raw[i])
        second = set(list(rucksack_raw[i+1]))
        third = list(rucksack_raw[i+2])
        common_candidates = second.intersection(first)
        common_item = common_candidates.intersection(third)
        score = ord(common_item.pop())
        if score >= 97:
            total_score += score - 96
        else:
            total_score += score - 38
        i += 3
    return total_score

if __name__=="__main__":
    print("Sum of common elements in the two sections is: ", get_common_item_score())
    print("Sum of common elements in the trios is: ", get_trio_common_item_score())
