def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for i in range(2, n):
        sum = a + b
        a = b
        b = sum
    return b


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()