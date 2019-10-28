def euclid(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


if __name__ == "__main__":
    print(euclid(84, 18))
