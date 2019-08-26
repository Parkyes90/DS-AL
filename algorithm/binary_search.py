def binary_search_rec(seq, target, low, high):
    if low > high:
        return None

    mid = (low + high) // 2

    if target == seq[mid]:
        return mid

    if target < seq[mid]:
        return binary_search_rec(seq, target, low, mid - 1)

    return binary_search_rec(seq, target, mid + 1, high)


def binary_search_iter(seq, target):
    high, low = len(seq), 0
    while low < high:
        mid = (high + low) // 2
        if target == seq[mid]:
            return mid

        if target < seq[mid]:
            high = mid
        else:
            low = mid

    return None


def test_binary_search():
    seq = [1, 2, 5, 6, 7, 10, 12, 12, 14, 15]
    print(binary_search_iter(seq, 6))
    print(binary_search_rec(seq, 6, 0, len(seq)))


if __name__ == "__main__":
    test_binary_search()
