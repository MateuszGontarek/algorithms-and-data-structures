def iteration_calculate(n):
    while n > 0:
        k = n**2
        print(k)
        n -= 1


def tail_recursion(n):
    if n > 0:
        k = n**2
        print(k)
        tail_recursion(n - 1)


def head_recursion(n):
    if n > 0:
        head_recursion(n - 1)
        k = n**2
        print(k)


def tree_calculate(n):
    if n > 0:
        tree_calculate(n - 1)
        k = n**2
        print(k)
        tree_calculate(n - 1)


tree_calculate(5)
