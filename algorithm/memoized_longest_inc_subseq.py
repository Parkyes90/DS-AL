from bisect import bisect
from itertools import combinations
from functools import wraps

from benchmark import benchmark


def native_longest_inc_subseq(seq):
    """simple"""
    for length in range(len(seq), 0, -1):
        for sub in combinations(seq, length):
            if list(sub) == sorted(sub):
                return len(sub)


def dp_longest_inc_subseq(seq):
    """dp"""
    l = [1] * len(seq)
    res = []
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                l[cur] = max(l[cur], 1 + l[pre])
    return max(l)


def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


def memoized_longest_inc_subseq(seq):
    """memoization"""

    @memo
    def l(cur):
        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max(res, 1 + l(pre))
        return res

    return max(l(i) for i in range(len(seq)))


def longest_inc_bisec(seq):
    """binary search"""
    end = []
    for val in seq:
        idx = bisect(end, val)
        if idx == len(end):
            end.append(val)
        else:
            end[idx] = val
    return len(end)


@benchmark
def test_native_longest_inc_subseq(s1):
    print(native_longest_inc_subseq(s1))


@benchmark
def test_dp_longest_inc_subseq(s1):
    print(dp_longest_inc_subseq(s1))


@benchmark
def test_memo_longest_inc_subseq(s1):
    print(memoized_longest_inc_subseq(s1))


@benchmark
def test_bisect_longest_inc_subseq(s1):
    print(longest_inc_bisec(s1))


if __name__ == "__main__":
    s1 = [94, 8, 78, 22, 38, 79, 93, 8, 84, 39]
    test_native_longest_inc_subseq(s1)
    test_dp_longest_inc_subseq(s1)
    test_memo_longest_inc_subseq(s1)
    test_dp_longest_inc_subseq(s1)
