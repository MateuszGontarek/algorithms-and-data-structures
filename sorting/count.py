def count(arr: list[int]) -> list[int]:
    B = [0] * (max(arr) + 1)

    sorted_arr = []
    for number in arr:
        B[number] += 1

    for i in range(len(B)):
        sorted_arr.extend([i] * B[i])

    return sorted_arr


array = [1, 8, 3, 5, 11, 2, 13, 6, 4, 7]
array = count(array)
print(array)
    