import time
from functools import wraps


def timeit(method):
    @wraps(method)
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if "log_time" in kw:
            name = kw.get("log_name", method.__name__.upper())
            kw["log_time"][name] = int((te - ts) * 1000)
        else:
            print("%r  %2.2f ms" % (method.__name__, (te - ts) * 1000))
        return result

    return timed


def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


def fib(n):
    if n < 2:
        return 1

    return fib(n - 1) + fib(n - 2)


@memo
def fib2(n):
    if n < 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)


def fib3(m, n):
    if m[n] == 0:
        m[n] = fib3(m, n - 1) + fib3(m, n - 2)
    return m[n]


@timeit
def test_fib(n):
    print(fib(n))


@timeit
def test_fib2(n):
    print(fib2(n))


@timeit
def test_fib3(n):
    m = [0] * (n + 1)
    m[0], m[1] = 1, 1
    print(fib3(m, n))


if __name__ == "__main__":
    n = 35
    test_fib(n)
    test_fib2(n)
    test_fib3(n)
