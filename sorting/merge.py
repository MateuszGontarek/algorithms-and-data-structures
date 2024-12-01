def merge(arr: list[int], left: int, mid: int, right: int) -> None:
    i = left
    j = mid + 1
    k = left
    sorted_arr = [0] * (right + 1)
    
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            sorted_arr[k] = arr[i]
            i += 1
        else:
            sorted_arr[k] = arr[j]
            j += 1
        k += 1
    
    while i <= mid:
        sorted_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        sorted_arr[k] = arr[j]
        j += 1
        k += 1

    for m in range(left, right + 1):
        arr[m] = sorted_arr[m]

def merge_sort(arr: list[int], left: int, right: int) -> list[int]:
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

arr_num = [3, 1 , 6 , 2 , 0, -1]

merge_sort(arr_num, 0, len(arr_num) - 1)

print(arr_num)
