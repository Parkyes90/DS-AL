def merge_sort(seq):
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]

    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    res = []

    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    #
    rev = []
    for i in range(len(res) - 1, -1, -1):
        rev.append(res[i])
    # print(rev, res)
    return (left or right) + rev


def merge_sort_sep(seq):
    if len(seq) < 2:
        return seq

    mid = len(seq) // 2
    left = merge_sort_sep(seq[:mid])
    right = merge_sort_sep(seq[mid:])
    return merge(left, right)


def merge(left, right):
    if not left or not right:
        return left or right
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[i])
            j += 1
    if left[i:]:
        result.extend(left[i:])
    if right[j:]:
        result.extend(right[j:])
    return result


def test_merge_sort():
    seq = [1, 5, 7, 20202, 1, 2, 5, 6, 7]
    print(merge_sort(seq))


def test_merge_sort_sep():
    seq = [1, 5, 7, 20202, 1, 2, 5, 6, 7]
    print(merge_sort_sep(seq))


if __name__ == "__main__":
    test_merge_sort()
    test_merge_sort_sep()
