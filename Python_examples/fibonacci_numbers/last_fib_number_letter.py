"""
Дано число 1 ≤ n ≤ 10^7,
необходимо найти последнюю цифру n n n-го числа Фибоначчи.

Если 0≤a,b≤9 — последние цифры чисел Fi​ и Fi+1 соответственно, то (a+b) mod 10 — последняя цифра числа Fi+2
"""
from pytest import mark


def get_last_fib_number_letter(n: 'int') -> 'int':
    if n == 0 or n == 1:
        return n

    previous = 0
    current = 1
    for _ in range(2, n + 1):
        previous, current = current % 10, (current + previous) % 10

    return current


def main():
    n = int(input())
    print(get_last_fib_number_letter(n))


if __name__ == "__main__":
    main()


@mark.parametrize('input_number,response', ((696352, 9), (4, 3), (5, 5), (6, 8), (7, 3)))
def test_simple_success(input_number: int, response: int):
    assert get_last_fib_number_letter(input_number) == response, f'Последняя цифра {input_number}-го числа Фибоначчи ' \
                                                                 'вычислена не верно'
