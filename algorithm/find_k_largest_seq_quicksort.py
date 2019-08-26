import random


def swap(seq, x, y):
    seq[x], seq[y] = seq[y], seq[x]


def quick_select(seq, k, left=None, right=None):
    left = left or 0
    right = right or len(seq) - 1
    ipivot = random.randint(left, right)
    pivot = seq[ipivot]

    swap(seq, ipivot, right)
    swap_index, i = left, left
    while i < right:
        if seq[i] < pivot:
            swap(seq, i, swap_index)
            swap_index += 1
        i += 1
    swap(seq, right, swap_index)
    rank = len(seq) - swap_index
    if k == rank:
        return seq[swap_index]

    if k < rank:
        return quick_select(seq, k, left=swap_index + 1, right=right)

    return quick_select(seq, k, left=left, right=swap_index - 1)


def find_k_largest_seq_quick_select(seq, k):
    kth_largest = quick_select(seq, k)
    result = []
    for item in seq:
        if item >= kth_largest:
            result.append(item)
    return result


if __name__ == "__main__":
    print(find_k_largest_seq_quick_select([3, 10, 4, 5, 1, 8, 9, 11, 5], 6))
