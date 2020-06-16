from random import randint

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def display(self):
        print("Rodzic: ", self.value)
        print("Dzieci: ", end = ' ')
        if self.left != None:
            print(self.left.value, end = ' ')
        else:
            print("None", end = ' ')
        if self.right != None:
            print(self.right.value, end = ' ')
        else:
            print("None", end = ' ')
        print("")
        print("")

def print_tree(tree):
    tree.display()
    if tree.left != None:
        print_tree(tree.left)
    if tree.right != None:
        print_tree(tree.right)

def random_gen(height):
    return randint(1, (height*50))

def generate(height, prev):
    if height > 0:
        left = Node(random_gen(height))
        right = Node(random_gen(height))
        prev.left = left
        prev.right = right
        generate(height - 1, left)
        generate(height - 1, right)

def prepare_tree(height):
    root = Node(random_gen(height))
    generate(height, root)
    return root

def dfs(tree):
    my_stack = []
    my_stack.append(tree)
    while len(my_stack) > 0:
        helper = my_stack.pop(0)
        yield helper.value
        if helper.right != None:
            my_stack.insert(0, helper.right)
        if helper.left != None:
            my_stack.insert(0, helper.left)

def bfs(tree):
    my_queue = []
    my_queue.append(tree)
    while len(my_queue) > 0:
        yield my_queue[0].value
        if my_queue[0].left != None:
            my_queue.append(my_queue[0].left)
        if my_queue[0].right != None:
            my_queue.append(my_queue[0].right)
        my_queue.pop(0)

def main():
    tree = prepare_tree(2)
    print_tree(tree)
    print("DFS: ", list(dfs(tree)))
    print("BFS: ", list(bfs(tree)))

main()
