import random as r

array = [r.randint(1, 20) for i in range(20)]
print(array)
for i in range(len(array) - 1):
    min_index = i
    j = i + 1
    for j in range(i + 1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]
print(array)
