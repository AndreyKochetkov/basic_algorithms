//
// Created by Андрей Кочетков on 02.02.17.
//

void bubbleSort(int *array, int size);
void swap_h(int &a, int &b);
void heap_insert(int *a, int n, int x);
void heap_pop(int *a, int n);
void heap_sort(int *data, int n);
void heap_make(int *a, int n);
void insertion_sort(int *a, int n);
void swap(int &a, int &b);
void selection_sort(int *a, int n);
void merge_sort(int *data, int size, int *buffer);
void merge(int *a, int a_len, int *b, int b_len, int *c);
void swap_q(int &a, int &b);
void merge_sort_fast(int *data, int size, int *buffer);
void quick_sort(int *a, int n);
int binary_search_rec(int* array, int key, int left, int right);
int binary_search_iter(int* array, int key, int right);