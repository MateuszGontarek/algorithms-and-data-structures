def radix(arr: list[int]):
    bins = [[] for _ in range(10)]
    max_element_lenght = len(str(max(arr)))

    for i in range(max_element_lenght):
        for number in arr:
            e = int(number / 10 ** i % 10)
            bins[e].append(number)
          
        k = 0
        for bin in bins:
            if not bin:
                continue
            
            for _ in range(len(bin)):
                arr[k] = bin.pop(0)
                k += 1

array = [1, 8, 3, 5, 11, 2, 13, 6, 4, 7]
radix(array)
print(array)



