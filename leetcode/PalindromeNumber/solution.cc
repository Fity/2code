#include<iostream>
using namespace std;


class Solution {
public:
    bool isPalindrome(int x) {
        int t = 0;
        if (x < 0){
            t = -x;
        }
        else{
            t = x;
        }
        int y = 0;
        while (t != 0) {
            y = y*10 + t%10;
            t /= 10;
        }
        return x == y;
    }
};
