#include<iostream>
using namespace std;


void exch(int arr[], int i, int j) {
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
    return;
}


void insert_sort(int arr[], int size) {
    for (int i=1; i<size; i++) {
        int j=i;
        while (j>0) {
            if (arr[j] > arr[j-1]) {
                break;
            }
            exch(arr, j, j-1);
            j--;
        }
    }
    return;
}


int main() {
    int arr[] = {9,8,7,6,5,4,3,2,1};
    insert_sort(arr, 9);
    for (int i=0; i<9; i++) {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}
