import itertools as it
import time

start = time.time()
for p in it.permutations(range(1, 10)):
    v = True
    for i in range(1, 10):
        if int("".join(map(str, p[:i]))) % i != 0:
            v = False
            continue
    if v:
        print("".join(map(str, p)))


time = time.time() - start
print("Time:", time)
