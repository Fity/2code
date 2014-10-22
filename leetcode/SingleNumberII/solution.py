#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one = 0
        amu = 0
        for x in A:
            amu |= x & one
            one ^= x
            t = amu & one
            one &= ~t
            amu &= ~t
        return one


def main():
    import random
    x = random.randint(1, 1000)
    l = [item for item in xrange(1, 1001) if item != x] * 3
    l.append(x)
    random.shuffle(l)
    so = Solution()
    rst = so.singleNumber(l)
    print 'x=', x
    if rst == x:
        print 'ok'


if __name__ == '__main__':
    for _ in xrange(10):
        main()
