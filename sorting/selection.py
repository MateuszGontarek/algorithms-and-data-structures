def selection_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr) - 1):
        index: int = i

        for j in range(i, len(arr)):
            if arr[index] > arr[j]:
                index = j

        arr[i], arr[index] = arr[index], arr[i]

    return arr



array = [1, 8, 3, 5, 11, 2, 13, 6, 4, 7]

print(selection_sort(array))