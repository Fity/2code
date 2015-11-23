#include<iostream>
using namespace std;


void exch(int arr[], int i, int j) {
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
    return;
}


void shell_sort(int arr[], int size) {
    int h = 1;
    while (h<size/3) {
        h = h*3+1;
    }
    while (h >= 1) {
        for( int i=h; i<size; i++){
            for (int j=i; j>=h; j-=h) {
                if (arr[j] > arr[j-h]) {
                    break;
                }
                exch(arr, j, j-h);
            }
        }
        h /= 3;
    }
    return;
}


int main() {
    int arr[] = {9,8,7,6,5,4,3,2,1};
    shell_sort(arr, 9);
    for(int i=0; i<9; i++) {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}
