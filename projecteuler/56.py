a = 0
for i in range(1, 100):
    for j in range(1, 100):
        a = max(a, sum(map(int, str(i**j))))
print(a)
