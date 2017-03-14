//
// Created by Андрей Кочетков on 03.02.17.
//

void quick_sort(int *a, int n) {
    int i = 0, j = n;        // поставить указатели на исходные места
    int temp, pivot;

    pivot = a[n >> 1];        // центральный элемент

    // процедура разделения
    do {
        while (a[i] < pivot) i++;
        while (a[j] > pivot) j--;

        if (i <= j) {
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
            i++;
            j--;
        }
    } while (i <= j);


    // рекурсивные вызовы, если есть, что сортировать
    if (j > 0) quick_sort(a, j);

    if (n > i) quick_sort(a + i, n - i);
}

