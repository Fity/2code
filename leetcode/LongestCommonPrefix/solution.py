# -*- coding:utf-8 -*-
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        prefix = []
        first = strs[0]
        if not first:
            return ''
        strs = strs[1:]
        for i, c in enumerate(first):
            for s in strs:
                if not s or i >= len(s):
                    break
                if s[i] != c:
                    break
            else:
                prefix.append(c)
                continue
            break
        return ''.join(prefix)
