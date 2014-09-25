# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution:

    def getLineSlope(self, pointPair):
        p1, p2 = pointPair
        if p1.x == p2.x:
            return 'none-'+str(p1.x)
        slope = 0
        if p1.y != p2.y:
            slope = 1.0*(p2.y - p1.y) / (p2.x - p1.x)
        # debug
        # if 3<slope<5:
        #     print 'point:', p1, p2
        intercept = p1.y - slope*p1.x
        # if abs(int(intercept)) == 70:
        #     print 'point:', p1, p2
        return str(slope)+'-'+str(intercept)

    def isEqual(self, p1, p2):
        return p1.x == p2.x and p1.y == p2.y

    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        # import itertools
        lineMap = {}
        max_num = 0
        if len(points) == 1:
            return 1
        if not points or len(points) == 0:
            return 0
        for index, a in enumerate(points):
            count = 0
            for b in points[index+1:]:
                if self.isEqual(a, b):
                    count += 1
                    continue
                lineSlope = self.getLineSlope((a, b))
                if lineSlope in lineMap:
                    lineMap[lineSlope] += 1
                else:
                    lineMap[lineSlope] = 1
            # print 'lineMap:', lineMap
            # print 'index:', index
            # print 'a:', list(points)
            count += 1
            if lineMap:
                count += max(lineMap.values())
            if count > max_num:
                max_num = count
                # print 'max_num:', max_num
                # print 'index:', index
                # print 'map:', lineMap
            lineMap.clear()
        return max_num
