from random import randint

from pytest import mark
from typing import List, Optional


def quick_sort(array: List[int], start: Optional[int] = None, end: Optional[int] = None) -> None:
    if not array:
        return
    if not start and not end:
        start = 0
        end = len(array) - 1
    left = start
    right = end
    pivot = array[int(left + (right - left) / 2)]
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    if right > start:
        quick_sort(array, start, right)
    if left < end:
        quick_sort(array, left, end)


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
    quick_sort(input_array)
    assert input_array == sorted_array


def test_random():
    for i in range(10):
        array = [randint(-10, 20) for i in range(50)]
        quick_sort(array)
        assert array == sorted(array)
