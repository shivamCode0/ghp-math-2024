c = 0


def reverse(n):
    return int(str(n)[::-1])


def is_palindrome(n):
    return n == reverse(n)


def is_lychrel(n):
    for i in range(50):
        n += reverse(n)
        if is_palindrome(n):
            return False
    return True


for i in range(1, 10000):
    if is_lychrel(i):
        c += 1

print(c)
