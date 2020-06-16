import time

def time_decorator(f):
    def print_time(*args, **kwargs):
        clk_start = time.process_time()
        z = f(*args, **kwargs)
        clk_stop = time.process_time()
        print("Excecution time: ", clk_stop - clk_start)
        return z
    return print_time


@time_decorator
def demo_func(x, y):
    for i in range(10):
        x += (x + y)*i
    return x


print(demo_func(3,4))
