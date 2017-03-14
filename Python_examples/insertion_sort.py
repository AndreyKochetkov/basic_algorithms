import random as r

array = [r.randint(1, 50) for i in range(30)]
print(array)
for i in range(1, len(array)):
    tmp = array[i]
    j = i
    while j > 0 and tmp < array[j -1]:
        array[j] = array[j - 1]
        j -= 1
    array[j] = tmp
print(array)
