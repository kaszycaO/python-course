from random import randint

def random_gen(height):
    return randint(1, (height*50))

def generate(height):
    el = random_gen(height)
    tree = [str(el), None, None]
    if height > 1:
        tree[1] = generate(height - 1)
        tree[2] = generate(height - 1)
    return tree

def dfs(tree):
    my_stack = []
    my_stack.append(tree)
    while len(my_stack) > 0:
        helper = my_stack.pop(0)
        yield helper[0]
        if helper[2] != None:
            my_stack.insert(0, helper[2])
        if helper[1] != None:
            my_stack.insert(0, helper[1])

def bfs(tree):
    my_queue = []
    my_queue.append(tree)
    while len(my_queue) > 0:
        yield my_queue[0][0]
        if my_queue[0][1] != None:
            my_queue.append(my_queue[0][1])
        if my_queue[0][2] != None:
            my_queue.append(my_queue[0][2])
        my_queue.pop(0)



def main():
    tree = generate(3)
    print(tree)
    print("DFS: ", list(dfs(tree)))
    print("BFS: ", list(bfs(tree)))

main()
