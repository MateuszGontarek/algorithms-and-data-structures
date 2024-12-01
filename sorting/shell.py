def shell(arr: list[int]) -> list[int]:
    n = len(arr)

    gap = n // 2
    
    while gap:
        i = gap
        while i < n:
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > arr[i]:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
            i += 1
        gap = gap // 2
    return arr


array = [1, 8, 3, 5, 11, 2, 13, 6, 4, 7]

print(shell(array))