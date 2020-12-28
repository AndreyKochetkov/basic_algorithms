from pytest import mark
from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    for i in range(len(array)):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]

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
    assert bubble_sort(input_array) == sorted_array
