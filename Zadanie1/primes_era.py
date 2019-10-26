def sieve(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)

    sqrt = n ** 0.5 + 1

    for i in range(1, int(sqrt)):
        j = i + 1
        while (i + 1) * j <= n:
            numbers[(i + 1) * j - 1] = 0
            j += 1

    result = []

    for i in numbers:
        if i != 0:
            result.append(i)
    result.remove(1)

    return result


if __name__ == "__main__":
    print(sieve(100))
