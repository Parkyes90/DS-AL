def quick_sort_cache(seq):
    if len(seq) < 2:
        return seq
    ipivot = len(seq) // 2
    pivot = seq[ipivot]

    before = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    after = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]
    return quick_sort_cache(before) + [pivot] + quick_sort_cache(after)


def partition_divided(seq):
    pivot, seq = seq[0], seq[1:]
    before = [x for x in seq if x <= pivot]
    after = [x for x in seq if x > pivot]
    return before, pivot, after


def quick_sort_cache_divided(seq):
    if len(seq) < 2:
        return seq
    before, pivot, after = partition_divided(seq)
    return quick_sort_cache(before) + [pivot] + quick_sort_cache_divided(after)


def test_quick_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    seq2 = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    print(quick_sort_cache(seq))
    print(quick_sort_cache_divided(seq2))


if __name__ == "__main__":
    test_quick_sort()
