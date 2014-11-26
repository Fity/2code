class Solution {
public:
    int lengthOfLastWord(const char *s) {
        char word[100] = "";
        int index = 0;
        bool inword = false;
        int lens_count = 0;
        for (int i=0; s[i] != '\0'; i++) {
            if (s[i] == ' ') {
                if (inword) {
                    inword = false;
                }
                continue;
            }
            else {
                if (!inword) {
                    index = 0;
                    inword = true;
                    lens_count = 0;
                }
                word[index] = s[i];
                lens_count++;
            }
        }
        return lens_count;
    }
};
