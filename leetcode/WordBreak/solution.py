#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean

    def wordBreak(self, s, wd):
        return self.wordBreakRec(s, wd, 0, {})

    def wordBreakRec(self, s, wd, index, rst):
        if not isinstance(wd, dict):
            wd = {w: True for w in wd}
        length = len(s)
        if index >= length:
            return True
        # if rst.get(index, None) is not None:
        if index in rst:
            return rst[index]
        i = index + 1
        while i <= length:
            if s[index:i] in wd:
                if self.wordBreakRec(s, wd, i, rst):
                    rst[i] = True
                    return True
                else:
                    rst[i] = False
            i += 1
        return False


if __name__ == '__main__':
    so = Solution()
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wd = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
          "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    print so.wordBreak(s, wd)
