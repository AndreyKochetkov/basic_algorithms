from random import randint

from pytest import mark
from typing import List

def merge_sort(array: List[int]) -> List[int]:
    if len(array) < 2:
        return array[:]
    else:
        middle = int(len(array) / 2)
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


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
    assert merge_sort(input_array) == sorted_array


def test_random():
    for i in range(10):
        array = [randint(-10, 20) for i in range(50)]
        assert merge_sort(array) == sorted(array)
