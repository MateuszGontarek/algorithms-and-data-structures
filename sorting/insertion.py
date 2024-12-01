def insertion(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        position = i
        value = arr[i]

        while position and arr[position - 1] > value:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = value
    
    return arr

array = [1, 8, 3, 5, 11, 2, 13, 6, 4, 7]

print(insertion(array))