#include<iostream>
using namespace std;


class Solution {
    public:
        int atoi(const char *str) {
            int neg = 3;
            int i = 0, lens = strlen(str);
            if (lens <= 0){
                return 0;
            }
            for(i = 0; i<lens; i++) {
                int c = str[i];
                if (c == ' ') {
                    continue;
                }
                if (c == '+' || c == '-' || isdigit(c)){
                    break;
                }
                return 0;
            }

            if (str[i] == '-') {
                neg = -1;
            }
            if (str[i] == '+' || str[i] == '-') {
                i++;
            }
            int ret = 0;
            for (; i<lens; i++){
                int c = str[i];
                if (str[i] == ' '){
                    break;
                }
                if (!isdigit(c)){
                    break;
                }
                c = c-'0';
                if (ret > 214748364){
                    if (neg == -1){
                        return -2147483648;
                    }
                    return 2147483647;
                }
                else if (ret == 214748364 && c > 7) {
                        if (neg == -1){
                            return -2147483648;
                        }
                        return 2147483647;
                }
                ret = ret * 10 + c;
            }
            if (neg == -1){
                ret = -ret;
            }
            return ret;
        }

};


int main(){
    char* arr[] = {"1", "+1", "-1", "-+1", "+-1", "0", "9876543210", "-9876543210", "  -0012a42"};
    int index = 0;
    Solution s;
    while (index < sizeof(arr)/sizeof(char *)) {
        cout<<s.atoi(arr[index])<<endl;
        index++;
    }
    string str;
    while (cin>>str) {
        cout<<s.atoi(str.c_str())<<endl;
    }
    return 0;
}
