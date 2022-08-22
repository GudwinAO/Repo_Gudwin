

def recursion(m, n):
    # Базовый случай
    if m == 0:
        return n + 1
    # Шаг рекурсии / рекурсивное условие
    elif n == 0 and m > 0:
        return recursion(m - 1, 1)
    # Шаг рекурсии / рекурсивное условие
    else:
        return recursion(m - 1, recursion(m, n - 1))


print(recursion(1, 100))


n = 1

n //= 2

print(n)

n %= 2

print(n)
