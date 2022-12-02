def get_moves():
    rps_file = open('advent2.txt', 'r')
    rps_raw = rps_file.readlines()
    rps_list = [r.replace('\n', '').replace(' ', '') for r in rps_raw]
    return rps_list

def rock_paper_scissors():
    rules = {'AX': 4, 'AY': 8, 'AZ': 3, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 7, 'CY': 2, 'CZ': 6}
    moves = get_moves()
    score = [rules[r] for r in moves]
    return sum(score)

def lose_draw_win():
    rules = {'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7}
    moves = get_moves()
    score = [rules[r] for r in moves]
    return sum(score)

if __name__=="__main__":
    print("Total score with approach 1: ", rock_paper_scissors())
    print("Total score with approach 2: ", lose_draw_win())