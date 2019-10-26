def wallis(n):
    result = 1.0
    for i in range(1, n + 1):
        result *= ((2 * i) ** 2) / ((2 * i - 1) * (2 * i + 1))
        print(result * 2)


if __name__ == "__main__":
    wallis(10)
