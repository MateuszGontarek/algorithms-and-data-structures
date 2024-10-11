def linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


array = [1, 3, 6, 8, 9, 11, 15, 18]

print(linear(array, 8))
