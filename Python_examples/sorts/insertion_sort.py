from random import randint

from pytest import mark
from typing import List


def insertion_sort(array: List[int]) -> List[int]:
    for i in range(1, len(array)):
        tmp = array[i]
        j = i
        while j > 0 and tmp < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = tmp

    return array


@mark.parametrize(
    'input_array, sorted_array',
    (
            ([3, 2, 1], [1, 2, 3]),
            ([], []),
            ([5, 6, 2, 1, 4], [1, 2, 4, 5, 6]),
            ([1, 2, 3, 4, 56], [1, 2, 3, 4, 56]),
    )
)
def test(input_array: List[int], sorted_array: List[int]):
    assert insertion_sort(input_array) == sorted_array


def test_random():
    for i in range(10):
        array = [randint(-10, 20) for i in range(50)]
        assert insertion_sort(array) == sorted(array)
