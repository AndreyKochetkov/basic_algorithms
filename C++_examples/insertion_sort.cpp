//
// Created by Андрей Кочетков on 02.02.17.
//
void insertion_sort(int *a, int n) {
    int j;
    for (int i = 1; i < n; ++i) {
        int tmp = a[i];
        for (j = i; j > 0 && tmp < a[j-1]; --j) {
            a[j] = a[j-1];
        }
        a[j] = tmp; }
}
