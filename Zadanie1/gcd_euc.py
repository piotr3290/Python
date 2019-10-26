def euclid(a, b):
    if b > a:
        temp = a
        a = b
        b = temp

    while b != 0:
        temp = a % b
        a = b
        b = temp

    return a


if __name__ == "__main__":
    print(euclid(84, 18))
