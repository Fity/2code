# -*- coding:utf-8 -*-
class Solution:
    # @return a string
    def countAndSay(self, n):
        say = '1'
        for x in xrange(n-1):
            count = 0
            ret = []
            prev = None
            for bit in say:
                if prev != bit:
                    if count:
                        ret.append(str(count))
                        ret.append(prev)
                    count = 1
                else:
                    count += 1
                prev = bit
            if count:
                ret.append(str(count))
                ret.append(prev)
            say = ''.join(ret)
        return say


if __name__ == '__main__':
    s = Solution()
    for n in xrange(10):
        print n, s.countAndSay(n)
