def selection_sort(seq):
    length = len(seq)
    for i in range(length - 1):
        min_j = i
        for j in range(i + 1, length):
            if seq[min_j] > seq[j]:
                min_j = j
        seq[i], seq[min_j] = seq[min_j], seq[i]
    return seq


def test_selection_sort():
    seq = [1, 5, 1, 2, 3, 4, 5, 2, 10, 4, 5]
    print(selection_sort(seq))
    print(seq)


if __name__ == "__main__":
    test_selection_sort()
