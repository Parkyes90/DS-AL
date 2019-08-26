import numpy


def quick_select_cache(seq, k):
    len_seq = len(seq)

    if k - 1 > len_seq:
        return None

    if len_seq < 2:
        return seq[0]

    ipivot = len_seq // 2
    pivot = seq[ipivot]

    smaller_list = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    larger_list = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]

    m = len(smaller_list)

    if k == m:
        return pivot

    if k < m:
        return quick_select_cache(smaller_list, k)

    return quick_select_cache(larger_list, k - m - 1)


def swap(seq, x, y):
    seq[x], seq[y] = seq[y], seq[x]


def quick_select(seq, k, left=None, right=None):
    left = left or 0
    right = right or len(seq) - 1
    ipivot = len(seq) // 2
    pivot = seq[ipivot]
    swap(seq, ipivot, right)
    swap_index, i = left, left

    while i < right:
        if pivot < seq[i]:
            swap(seq, i, swap_index)
            swap_index += 1
        i += 1

    swap(seq, right, swap_index)
    rank = len(seq) - swap_index
    if k == rank:
        return seq[swap_index]

    if k < rank:
        return quick_select(seq, k, swap_index + 1, right)

    return quick_select(seq, k, left, swap_index - 1)


if __name__ == "__main__":
    seq = [3, 7, 2, 1, 4, 6, 5, 10, 9, 11]
    k = len(seq) // 2
    print(sorted(seq))
    print(quick_select_cache(seq, 20), "cache")
    print(quick_select(seq, k))
    print(numpy.median(seq))
