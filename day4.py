def get_pairs():
    pairs_file = open('advent4.txt', 'r')
    pairs_raw = pairs_file.read().splitlines()
    return pairs_raw

def get_num_fully_overlap():
    pairs_raw = get_pairs()
    num_overlaps = 0
    for line in pairs_raw:
        pairs = line.split(',')
        first_pair = pairs[0].split('-')
        second_pair = pairs[1].split('-')
        if (fully_contained(first_pair, second_pair)):
            num_overlaps += 1
        elif (fully_contained(second_pair, first_pair)):
            num_overlaps += 1
    return num_overlaps

def get_num_partial_overlap():
    pairs_raw = get_pairs()
    num_not_overlap = 0
    for line in pairs_raw:
        pairs = line.split(',')
        first_pair = pairs[0].split('-')
        second_pair = pairs[1].split('-')
        if (not_overlap_at_all(first_pair, second_pair)):
            num_not_overlap += 1
        elif (not_overlap_at_all(second_pair, first_pair)):
            num_not_overlap += 1
    return len(pairs_raw) - num_not_overlap

def fully_contained(a, b):
    return int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1]) 

def not_overlap_at_all(a, b):
    return int(a[1]) < int(b[0])


if __name__=="__main__":
    print("Number of pairs that fully overlap: ", get_num_fully_overlap())
    print("Number of pairs that partially overlap: ", get_num_partial_overlap())