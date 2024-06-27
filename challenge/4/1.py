q = 1e4
q1 = -1
for i in range(10000, 100000):
    a = sum(map(int, str(i)))
    # print(i, a)
    b = i // a
    if b == i / a:
        if b < q:
            q = b
            q1 = i
            print(q, q1, b, a, i)

print(q, q1)
