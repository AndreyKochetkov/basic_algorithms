#include <iostream>
#include "sorts.h"

using namespace std;

void sieve2();
int main() {
    int size = 11;
    //int array[] = {1,2,4,4,4,4,4,5,6,7,8};
    int *array = new int[size];
    for (int i = 0; i < size; i++) {
        array[i] = rand() % 101;
    }
    for (int i = 0; i < size; i++) {
        cout << array[i] << " ";
    }

    cout << endl;
    //selection_sort(array, size);
    insertion_sort(array, size);
    //bubbleSort(array, size);

    //heap_maie(array, size);

    /*for(int i = 0; i < size; i++){
        cout << array[i] << endl;
    }
    cout << endl;

    heap_sort(array, size);
    */

    int buffer[size];
    //merge_sort(array, size, buffer);
    //merge_sort_fast(array, size, buffer);

    //quick_sort(array, size);



    for (int i = 0; i < size; i++) {
        cout << array[i] << " ";
    }
    cout << endl;

    int index =  binary_search_rec(array, 4, 0, 10);

    cout << endl << index << endl;

    return 0;
}


void sieve2() {
    int size = 30;
    int array[size + 1];
    int buffer[size + 1];
    int count = 0;
    // заполняем решето единицами
    for (int i = 1; i <= size; i++) {
        buffer[i] = -1;
        array[i] = 1;
    }

    for (int i = 2; i <= size; i++) {
        // если 2i+1 - простое (т. е. i не вычеркнуто)
        if (array[i] == 1) {
            buffer[count] = i;
            count++;
            // то вычеркнем кратные 2i+1
            for (int j = i * 2; j <= size; j += i) {
                array[j] = 0;
            }
        }
    }
    for (int i = 0; i < count; ++i) {
        cout << buffer[i] << endl;
    }
}



