#include<iostream>
using namespace std;


void exch(int seq[], int i, int j) {
    int tmp = seq[i];
    seq[i] = seq[j];
    seq[j] = tmp;
    return;
}


void select(int seq[], int size) {
    for (int i=0; i<size; i++) {
        int cur = i;
        for (int j=i+1; j<size; j++) {
            if (seq[j] > seq[cur]) {
                cur = j;
            }
        }
        exch(seq, i, cur);
    }
    return;
}


int main() {
    int arr[] = {1,2,3,4,5,6,7,8,9};
    select(arr, 9);
    for (int i=0; i<9; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}
