from random import randint

from pytest import mark
from typing import List


def selection_sort(array: List[int]) -> List[int]:
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

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
    assert selection_sort(input_array) == sorted_array


def test_random():
    for i in range(10):
        array = [randint(-10, 20) for i in range(50)]
        assert selection_sort(array) == sorted(array)
