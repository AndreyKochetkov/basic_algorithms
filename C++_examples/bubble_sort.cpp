//
// Crearrayted by Андрей Кочетков on 02.02.17.
//



void bubbleSort(int *array, int size) {
    int i, j;
    int temp;
    for (i = 0; i < size; i++) {
        for (j = size - 1; j > i; j--) {
            if (array[j - 1] > array[j]) {
                temp = array[j - 1];
                array[j - 1] = array[j];
                array[j] = temp;
            }
        }
    }
}