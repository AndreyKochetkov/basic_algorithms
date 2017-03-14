//
// Created by Андрей Кочетков on 02.02.17.
//

void swap_m(int &a, int &b) {
    int tmp = a;
    a = b;
    b = tmp;
}

void merge(int *a, int a_len, int *b, int b_len, int *c) {
    int i = 0;
    int j = 0;
    for (; i < a_len and j < b_len;) {
        if (a[i] < b[j]) {
            c[i + j] = a[i];
            ++i;
        } else {
            c[i + j] = b[j];
            ++j;
        }
    }
    if (i == a_len) {
        for (; j < b_len; ++j) { c[i + j] = b[j]; }
    } else {
        for (; i < a_len; ++i) { c[i + j] = a[i]; }
    }
}


void merge_sort(int *data, int size, int *buffer) {
    if (size < 2) return;
    merge_sort(data, size / 2, buffer);
    merge_sort(&data[size / 2], size - size / 2, buffer);

    merge(&data[0], size / 2, &data[size / 2], size - size / 2, buffer);

    for (int pos = 0; pos < size; ++pos) {
        data[pos] = buffer[pos];
    }
}

void merge_sort_fast(int *data, int size, int *buffer) {
    bool is_swapped = false;
    for (int chunk_size = 1; chunk_size < size; chunk_size *= 2, is_swapped = !is_swapped) {
        int offset = 0;
        for (; offset + chunk_size < size; offset += 2 * chunk_size) {
            int right_size = chunk_size;
            if (offset + chunk_size + right_size > size) {
                right_size = size - offset - chunk_size;
            }
            merge(
                    &data[offset], chunk_size,
                    &data[offset + chunk_size], right_size,
                    &buffer[offset]);
        }
        for (int pos = offset; pos < size; ++pos) {
            buffer[pos] = data[pos];
        }
        int * t = data;
        data = buffer;
        buffer = t;
    }

    if (is_swapped) {
        int * t = data;
        data = buffer;
        buffer = t;
        for (
                int pos = 0;
                pos < size;
                ++pos) {
            data[pos] = buffer[pos];
        }
    }
}
