import math

f = math.factorial

c = 0
for i in range(1, 101):
    for j in range(1, i):
        if f(i) / (f(j) * f(i - j)) > 1000000:
            c += 1
print(c)
