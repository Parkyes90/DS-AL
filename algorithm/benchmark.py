from functools import wraps
import time


def benchmark(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print("{0}: {1:0.2f} ms".format(func.__name__, ((end - start) * 1000)))
        return ret

    return wrap
