"""
Дано целое число 1≤n≤40,
необходимо вычислить n n n-е число Фибоначчи.
F0=0, F1=1 и Fn = Fn−1 + Fn−2 при n≥2
"""
from pytest import mark


def get_n_fib_number(n: 'int') -> 'int':
    if n == 0 or n == 1:
        return n

    previous = 0
    current = 1
    for _ in range(2, n + 1):
        previous, current = current, current + previous

    return current


def main():
    n = int(input())
    print(get_n_fib_number(n))


if __name__ == "__main__":
    main()


@mark.parametrize('input_number,response', ((3, 2), (4, 3), (5, 5), (6, 8), (7, 13)))
def test_simple_success(input_number: int, response: int):
    assert get_n_fib_number(input_number) == response, f'{input_number}-е число Фибоначчи вычисленно не верно'
