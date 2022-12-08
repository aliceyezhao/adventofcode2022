class Tree:
    def __init__(self, data):
        self.children = []
        self.data = data
        self.size = 0
        self.parent = None

def construct_tree():
    dir_file = open('advent7.txt', 'r')
    dir_instructions = dir_file.read().splitlines()
    dir_tree = Tree('/')
    sub_tree = []
    curr_node = dir_tree
    for instruction in dir_instructions[1:]:
        ins = instruction.split()
        first, second = ins[0], ins[1]
        if first == 'dir':
            node = Tree(second)
            node.parent = curr_node
            sub_tree.append(node)
        elif first.isdigit():
            node = Tree(second)
            node.size = int(first)
            node.parent = curr_node
            sub_tree.append(node)
        elif second == 'cd':
            if curr_node.children == []:
                curr_node.children = sub_tree
                
            if ins[2] == '..':
                curr_node = curr_node.parent
            else:
                children_values = [t.data for t in curr_node.children]
                curr_node_index = children_values.index(ins[2])
                curr_node = curr_node.children[curr_node_index]
            sub_tree = []

    curr_node.children = sub_tree
    return dir_tree

def get_dir_sizes():
    max_size = 100000
    tree = construct_tree()
    dir_sizes = next_level(tree, [])
    return sum([s for s in dir_sizes if s <= max_size])        

def next_level(tree, dir_sizes):
    for node in tree.children:
        if node.size == 0:
            size = sum_children(node, 0)
            dir_sizes.append(size)
            node.size = size
            next_level(node, dir_sizes)
    return dir_sizes

def sum_children(node, size):
    if node.size > 0:
        return node.size
    else:
        for child in node.children:
            size += sum_children(child, 0)
        return size

def get_tree_size():
    dir_file = open('advent7.txt', 'r')
    dir_instructions = dir_file.read().splitlines()
    size = 0
    for instruction in dir_instructions:
        ins = instruction.split()
        if ins[0].isdigit():
            size += int(ins[0])
    return size


def get_min_dir_to_delete():
    disk_size = 70000000
    space_needed = 30000000
    tree = construct_tree()
    tree_size = get_tree_size()
    dir_sizes = next_level(tree, [])
    space_avail = disk_size - tree_size
    space_to_clear = space_needed - space_avail
    return min([dir for dir in dir_sizes if dir >= space_to_clear])


            
if __name__=="__main__":
    print("The sum of directory sizes less than 100000 is: ", get_dir_sizes())
    print("The size of the smallest dirctory to delete to free up space is: ", get_min_dir_to_delete())
