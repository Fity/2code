#include<iostream>
#include<cmath>
using namespace std;


int reverse(int x){
    int ret = 0;
    while (x != 0) {
        if (abs(ret) > 214748364) {
            return 0;
        }
        ret = ret * 10 + x % 10;
        x /= 10;
    }
    return ret;
}


int main(){
    cout<<x<<endl;
    cout<<reverse(x)<<endl;
    return 0;
}
