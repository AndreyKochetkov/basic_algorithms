"""
Generator of fibonacci numbers
input: amount of numbers
"""
from typing import Iterator


def fibonacci(limit: int = 10) -> Iterator[int]:
    yield 1
    yield 1
    prev = 1
    current = 1
    limit -= 2
    while limit:
        prev, current = current, prev + current
        yield current
        limit -= 1


def main():
    n = int(input())
    print(fibonacci(n))


if __name__ == "__main__":
    main()


def test_success():
    generator = fibonacci(10)
    assert [1, 1, 2, 3, 5, 8, 13, 21, 34, 55] == [i for i in generator], 'Неверные числа Фибоначчи'
