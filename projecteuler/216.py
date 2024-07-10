from tqdm import trange

primes = [2]


def is_prime(n):
    if n < 2:
        return False
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return False
    primes.append(n)
    return True


for i in trange(3, 50_000_001, 2):
    is_prime(i)

print(is_prime(10**9 + 7))  # True, 10^9 + 7 is a prime
print(is_prime(10**9 + 8))  # False, 10^9 + 8 is not a prime


def t(n):
    return 2 * n * n - 1


c = 0

# for i in trange(2, 50000001):
#     if is_prime(t(i)):
#         c += 1

# print(c)
