import math, itertools as it
import numba as nb


def count_factors(n):
    f = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if i * i == n:
            f += 1
        elif n % i == 0:
            f += 2
    return f


@nb.jit(nopython=True)
def count_factors2(n):
    f = 0
    i = 1
    while i * i < n + 1:
        if n % i == 0:
            f += 1
        i += 1
    return f


print(count_factors2(12))  # 6
print(count_factors2(17))  # 6
print(count_factors2(360))  # 6

n = 1
while True:
    if count_factors(n**2) > 1000:
        print(f"Solved: {n}")
        break
    n += 1
    if n % 10000 == 0:
        print(n)
