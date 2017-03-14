import random as r

array = [r.randint(1, 50) for i in range(40)]
print(array)


def quick_sort(array, start, end):
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


quick_sort(array, 0, len(array) - 1)

print(array)
