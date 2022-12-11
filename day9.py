def is_touching(head, tail):
    x = abs(head[0] - tail[0])
    y = abs(head[1] - tail[1])
    return x <= 1 and y <= 1

def to_tuple(coords):
    return (coords[0], coords[1])

def update_head(head, direction):
    if direction == 'R':
        head[0] += 1
    elif direction == 'L':
        head[0] -= 1
    elif direction == 'U':
        head[1] += 1
    elif direction == 'D':
        head[1] -= 1
    return 

def update_tail(head, tail, direction):
    if is_touching(head, tail):
        return 
    elif head[0] == tail[0] and head[1] > tail[1]:
        tail[1] += 1
    elif head[0] > tail[0] and head[1] > tail[1]:
        tail[0] += 1
        tail[1] += 1
    elif head[0] < tail[0] and head[1] > tail[1]:
        tail[0] -= 1
        tail[1] += 1
    elif head[0] < tail[0] and head[1] == tail[1]:
        tail[0] -= 1
    elif head[0] < tail[0] and head[1] < tail[1]:
        tail[0] -= 1
        tail[1] -= 1
    elif head[0] == tail[0] and head[1] < tail[1]:
        tail[1] -= 1
    elif head[0] > tail[0] and head[1] < tail[1]:
        tail[0] += 1
        tail[1] -= 1
    elif head[0] > tail[0] and head[1] == tail[1]:
        tail[0] += 1
    return

def get_path_knots(knots):
    steps_raw = open('advent9.txt', 'r').readlines()
    steps = [step.replace('\n', '').split() for step in steps_raw]
    k = knots - 1
    head, tail = [0,0], [[0,0] for _ in range(k)]
    visited = set()
    visited.add(to_tuple(tail[k-1]))
    for step in steps:
        n = int(step[1])
        for _ in range(n):
            update_head(head, step[0]) 
            for i in range(k):
                if i == 0:
                    update_tail(head, tail[i], step[0])
                else: 
                    update_tail(tail[i-1], tail[i], step[0])
            visited.add(to_tuple(tail[k-1]))
    return len(visited)

if __name__ == "__main__":
    print("The tail of the rope with 2 knots touches this visits this many positions: ", get_path_knots(2))
    print("The tail of the rope with 10 knots touches this visits this many positions: ", get_path_knots(10))
