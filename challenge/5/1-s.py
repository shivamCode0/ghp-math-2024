import itertools as it

def count(n):
    a = str(n)
    b = [0] * 10
    for i in range(0, 10): b[i] = a.count(str(i))
    return b

v = count(234_235_28)
for a, b, c in it.permutations(range(0, 10), 3):
    abc = a * 100 + b * 10 + c
    bca = b * 100 + c * 10 + a
    cab = c * 100 + a * 10 + b
    t = abc * bca * cab
    if count(t // 10) == v: print(t, a, b, c)
