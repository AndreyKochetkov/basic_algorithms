from pytest import mark


def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a

    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()


@mark.parametrize('first,second,result', ((10, 5, 5), (10, 6, 2), (3918848, 1653264, 61232)))
def test_simple_success(first: int, second: int, result: int):
    assert gcd(first, second) == result, f'{result} не является НОД {first} и {second}'
