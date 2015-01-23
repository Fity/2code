# -*- coding:utf-8 -*-
ass Solution:
    # @return a string
    def convertToTitle(self, num):
        l = []
        while num > 0:
            c = chr((num-1) % 26 + ord('A'))
            l.append(c)
            num = (num-1) // 26
        return ''.join(l[::-1])
