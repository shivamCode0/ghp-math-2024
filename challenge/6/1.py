import sympy as sp
import numpy as np
import math


# make polynomial product from 0 to n of (1+x*2^n)
x = sp.Symbol("x")


def make_poly(n):
    poly = 1
    for i in range(n + 1):
        poly *= 1 + x * 2**i
    # print(f"n = {n}, poly = {poly}")
    return poly


# find coefficients of x^2
def find_coefficient_x2(n):
    poly = make_poly(n)
    poly = sp.expand(poly)
    return poly.coeff(x**2)


def find_coefficient_x2_v2(n):
    # (2 - 3*2^n + 4^n)/3
    v = n + 1
    return (2 - 3 * 2**v + 4**v) // 3


q = []
for i in range(0, 200):
    c = find_coefficient_x2(i)
    c2 = find_coefficient_x2_v2(i)
    assert c == c2, f"{i=} {c=} {c2=}"
    q.append(c)
    print(i, c, c2)

print(",".join(map(str, q)))
