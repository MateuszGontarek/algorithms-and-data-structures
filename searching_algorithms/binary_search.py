def binary_search(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l + r) // 2

        if arr[m] == target:
            return m
        elif arr[m] > target:
            r = m - 1
        else:
            l = m + 1

    return -1


def binary_search_rec(arr, target, l=0, r=0):
    if not r:
        r = len(arr) - 1

    m = (l + r) // 2

    if l > r:
        return -1

    if arr[m] == target:
        return m
    elif arr[m] > target:
        return binary_search_rec(arr, target, l, m - 1)
    else:
        return binary_search_rec(arr, target, m + 1, r)


array = [1, 3, 6, 8, 9, 11, 15, 18]

print(binary_search_rec(array, 9))
