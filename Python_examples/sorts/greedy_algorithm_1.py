def gal(l):
    out = []
    while True:
        sort_cust(l)
        right_end = l.pop(0)[1]
        for i in range(len(l)):
            if right_end >= l[0][0]:
                l.pop(0)
        out.append(right_end)
        if len(l) == 0:
            break
    return out


def sort_cust(array):
    for i in range(len(array) - 1):
        min_index = i
        j = i + 1
        for j in range(i + 1, len(array)):
            if array[j][1] < array[min_index][1]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array


def main():
    n = int(input())
    l = []
    for i in range(n):
        a, b = map(int, input().split())
        l.append((a, b))
    out = gal(l)
    sen = ""
    print(len(out))
    for i in out:
        sen += str(i) + " "
    print(sen)


if __name__ == "__main__":
    main()
