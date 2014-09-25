class Solution:

# @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict_num = dict.fromkeys(num, 1)
        for index, item in enumerate(num):
            if (target - item) not in dict_num:
                continue
            for tindex, cab in enumerate(num[index + 1:]):
                if item + cab == target:
                    return (index + 1, index + tindex + 2)


def main():
    import random
    num = [random.randint(1, 1000) for x in xrange(10)]
    print num
    a = int(random.uniform(0, 10))
    b = int(random.uniform(0, 10))
    while a == b:
        b = int(random.uniform(0, 10))
    if a > b:
        a, b = b, a
    target = num[a] + num[b]
    a += 1
    b += 1
    # num = [0, 3, 3, 4]
    # target = 7
    # a = 2
    # b = 4
    print a, b, target
    x, y = Solution().twoSum(num, target)
    print x, y, num[x - 1] + num[y - 1]

if __name__ == '__main__':
    main()
