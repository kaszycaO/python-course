import math
from inspect import getfullargspec



class Functions(object):
    def __init__(self):
        self.funcs = {}

    def __call__(self, *args):
        func = self.funcs.get(str(len(args)))
        return func(*args)

    def add_func(self, args_len, func):
        self.funcs[str(args_len)] = func

memory = Functions()

def overload():
    def modified(func):
        size = getfullargspec(func).args
        memory.add_func(len(size), func)
        return memory
    return modified

@overload()
def norm(x,y):
    return math.sqrt(x*x + y*y)

@overload()
def norm(x,y,z):
    return abs(x) + abs(y) + abs(z)


def main():
    print(f"norm(2,4) = {norm(2,4)}")
    print(f"norm(2,3,4) = {norm(2,3,4)}")


main()
