import primes_era


def lcm(a, b):
    if a > b:
        numbers_p = primes_era.sieve(a)
    else:
        numbers_p = primes_era.sieve(b)

    final_amount = []

    i = 0

    while a != 1 or b != 1:

        amount = 0

        while a % numbers_p[i] == 0:
            amount += 1
            a /= numbers_p[i]

        final_amount.append([numbers_p[i], amount])
        amount = 0

        while b % numbers_p[i] == 0:
            amount += 1
            b /= numbers_p[i]

        if final_amount[-1][1] < amount:
            final_amount[-1][1] = amount

        if final_amount[-1][1] == 0:
            final_amount.pop()

        i += 1

    result = 1

    for i in range(len(final_amount)):
        result *= final_amount[i][0] ** final_amount[i][1]
    return result


if __name__ == "__main__":
    print(lcm(192, 348))
