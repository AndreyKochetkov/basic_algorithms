//
// Created by Андрей Кочетков on 22.02.17.
//

int binary_search_rec(int *array, int key, int left, int right)  {
    int mid = left + (right - left) / 2;

    if (left >= right)
        return -(1 + left);

    if (array[left] == key)
        return left;

    if (array[mid] == key) {
        if (mid == left + 1)
            return mid;
        else
            return binary_search_rec(array, key, left, mid + 1);
    } else if ((array[mid] > key))
        return binary_search_rec(array, key, left, mid);
    else
        return binary_search_rec(array, key, mid + 1, right);
}

int binary_search_iter(int* array, int key, int right) {
    int left = 0;
    int mid = 0;

    while (left < right) {

        if (array[left] == key)
            return left;

        mid = left + (right - left) / 2;

        if (array[mid] == key) {
            if (mid == left + 1)
                return mid;
            else
                right = mid + 1;
        } else if ((array[mid] > key))
            right = mid;
        else
            left = mid + 1;
    }

    return -(1 + left);
}

/*
int binary_search_rec(int* array, int key, int left, int right) {
    int mid = left + (right - left) / 2;

    if (left >= right)
        return -(1 + left);

    if (array[mid] == key)
        return mid;

    else if (array[mid] > key)
        return binary_search_rec(array, key, left, mid);
    else
        return binary_search_rec(array, key, mid + 1, right);
}
*/

