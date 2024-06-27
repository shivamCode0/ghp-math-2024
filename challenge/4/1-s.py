q = 1e4
for i in range(10000, 100000):
    a = sum(map(int, str(i)))
    b = i // a
    if b == i / a and b < q: q = b
print(q)
