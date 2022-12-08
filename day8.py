import numpy as np

forest_raw = open('advent8.txt', 'r').readlines()
forest = np.array([list(f.replace('\n', '')) for f in forest_raw])
width = len(forest[0])
height = len(forest)

def get_visibility():
    num_visible = 0
    for row in range(len(forest)):
        for col in range(len(forest[0])):
            if visible_top(row, col) or visible_bottom(row, col) or visible_left(row, col) or visible_right(row, col):
                num_visible += 1
    return num_visible 

def visible_top(row, col):
    if row == 0:
        return True
    tree = forest[row][col]
    trees_in_the_way = forest[:,col][:row]
    return max(trees_in_the_way) < tree

def visible_bottom(row, col):
    if row == height - 1:
        return True
    tree = forest[row][col]
    trees_in_the_way = forest[:,col][row+1:]
    return max(trees_in_the_way) < tree
    
def visible_left(row, col):
    if col == 0:
        return True
    tree = forest[row][col]
    trees_in_the_way = forest[row][:col]
    return max(trees_in_the_way) < tree
    
def visible_right(row, col):
    if col == width - 1:
        return True
    tree = forest[row][col]
    trees_in_the_way = forest[row][col+1:]
    return max(trees_in_the_way) < tree

def get_view_score():
    max_view = 0
    for row in range(len(forest)):
        for col in range(len(forest[0])):
            tree_view = top_view(row, col) * bottom_view(row, col) * left_view(row, col) * right_view(row, col)
            # print(forest[row][col], tree_view)
            max_view = max(max_view, tree_view)
    return max_view

def top_view(row, col):
    if row == 0:
        return 0
    tree = forest[row][col]
    trees_in_the_way = forest[:,col][:row]
    return get_num_in_view(tree, np.flip(trees_in_the_way))

def bottom_view(row, col):
    if row == height - 1:
        return 0
    tree = forest[row][col]
    trees_in_the_way = forest[:,col][row+1:]
    return get_num_in_view(tree, trees_in_the_way)

def left_view(row, col):
    if col == 0:
        return 0
    tree = forest[row][col]
    trees_in_the_way = forest[row][:col]
    return get_num_in_view(tree, np.flip(trees_in_the_way))

def right_view(row, col):
    if col == width - 1:
        return 0
    tree = forest[row][col]
    trees_in_the_way = forest[row][col+1:]
    return get_num_in_view(tree, trees_in_the_way)

def get_num_in_view(tree, trees_in_the_way):
    if len(trees_in_the_way) <= 1:
        return len(trees_in_the_way)
    non_blocking_trees = []
    for t in trees_in_the_way:
        if t < tree:
            non_blocking_trees.append(t)
        else:
            return len(non_blocking_trees) + 1
    return len(non_blocking_trees) 


if __name__ == "__main__":
    print("The number of trees visible from the edges is: ", get_visibility())
    print("The highest view score is: ", get_view_score())
