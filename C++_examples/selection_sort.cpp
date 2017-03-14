//
// Created by Андрей Кочетков on 02.02.17.
//

void swap(int &a, int &b) {
    int tmp = a;
    a = b;
    b = tmp;
}

void selection_sort(int *a, int n) {
    for (int i = 0; i < n - 1; ++i) {
        int min_index = i;
        for (int j = i + 1; j < n; ++j) {
            if (a[j] < a[min_index]) min_index = j;
        }
        swap(a[i], a[min_index]);
    }
}

