def partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[low]
    i = low
    j = high
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quicksort(arr: list[int], low: int, high: int):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
    
array = [1, 8, 3, 5, 11, 2, 13, 6, 4, 7]
quicksort(array, 0, len(array) - 1)
print(array)