primes_1k = [2]
for n in range(3, 1000, 2):
    for p in primes_1k:
        if n % p == 0:
            break
        if p * p > n:
            primes_1k.append(n)
            break
    else:
        primes_1k.append(n)


print(primes_1k)
print(len(primes_1k))

best = -1, -1, -1  # length, a, b
for a in range(-999, 1000):
    for b in primes_1k:
        n = 0
        while n * n + a * n + b in primes_1k:
            n += 1
        if n > best[0]:
            best = n, a, b

print(best)
print(best[1] * best[2])
