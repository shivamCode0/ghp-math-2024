import fractions, math
from tqdm import trange


def f(n):
    a = 1
    for i in range(n):
        a = 1 + fractions.Fraction(1, 1 + a)

    return a


q = 0
for i in trange(1, 1001):
    a = f(i)
    if len(str(a.numerator)) > len(str(a.denominator)):
        q += 1

print(q)
