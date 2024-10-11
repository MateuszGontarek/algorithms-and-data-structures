def sum_natural(n, total=0):
    if not n:
        return total

    return sum_natural(n - 1, total + n)


print(sum_natural(5))
