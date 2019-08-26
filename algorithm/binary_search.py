from math import sqrt


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


def find_value_in_matrix(matrix, value):
    if not (len(matrix) > 0 and len(matrix[0])) > 0:
        return None

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == value:
                return True

    return False


def searching_in_a_sorted_matrix(m1, value):
    rows = len(m1)
    cols = len(m1[0])
    lo = 0
    hi = rows * cols
    while lo < hi:
        mid = (lo + hi) // 2
        row = mid // cols
        col = mid % rows
        v = m1[row][col]
        if v == value:
            return True

        if v > value:
            hi = mid
        else:
            lo = mid + 1
    return False


def find_max_unimodal_array(a):
    if len(a) < 2:
        return None

    left = 0
    right = len(a) - 1
    while right > left + 1:
        mid = (left + right) // 2
        if a[mid] > a[mid - 1] and a[mid] > a[mid + 1]:
            return a[mid]

        if a[mid - 1] < a[mid] < a[mid + 1]:
            left = mid
        else:
            right = mid
    return None


def find_sqrt_bin_search(n, error=0.000001):
    lower = n if n < 1 else 1
    upper = 1 if n < 1 else n
    mid = (upper + lower) / 2.0
    square = mid * mid
    count = 0
    while abs(square - n) > error:
        count += 1
        print(count)
        if square < n:
            lower = mid
        else:
            upper = mid
        mid = (upper + lower) / 2.0
        square = mid * mid
    return mid


def test_searching_in_a_matrix():
    a = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    print(searching_in_a_sorted_matrix(a, 13))


if __name__ == "__main__":
    test_searching_in_a_matrix()
    print(find_sqrt_bin_search(3), sqrt(3))
