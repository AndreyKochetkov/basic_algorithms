def fib_mod(n, m):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for i in range(2, n):
        a %= m
        b %= m
        sum = (a + b) % m
        a = b
        b = sum
    return b % m


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
