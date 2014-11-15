#include<iostream>
using namespace std;


class Solution {
public:
    bool isPalindrome(string s) {
        if (s.empty()){
            return true;
        }
        int lens = s.size() - 1;
        int begin=0, end=lens;
        while (true) {
            while (begin <= end && !isalnum(s[begin])) {
                begin++;
            }
            while (end >= 0 && !isalnum(s[end])) {
                end--;
            }
            if (begin >= end) {
                return true;
            }
            if (tolower(s[begin]) != tolower(s[end])) {
                return false;
            }
            begin++;
            end--;
        }
        return true;
    }
};


int main(){
    Solution s;
    cout<<s.isPalindrome("A man, a plan, a canal: Panama")<<endl;
    cout<<s.isPalindrome("race a car")<<endl;
    cout<<s.isPalindrome(".,")<<endl;
    cout<<s.isPalindrome(" ")<<endl;
    string str;
    while (cin>>str) {
        cout<<s.isPalindrome(str)<<endl;
    }
    return 0;
}
