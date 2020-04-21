"""
Проверка нахождения ключа в массиве
"""

from typing import List
from pytest import mark


def bin(array: List[int], key: int) -> bool:
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if array[mid] == key:
            return True
        if array[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return False


def main():
    array = [int(x) for x in input().split(' ')]
    key = int(input())
    print(bin(array, key))


if __name__ == "__main__":
    main()


@mark.parametrize('key, response', ((8, True), (1, True), (23, False), (1, True), (11, False)))
def test_success(key, response):
    array = [1, 5, 8, 12, 13]
    assert bin(array, key) is response
