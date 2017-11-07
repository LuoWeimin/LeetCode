#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(points)):
            dis = {}
            for j in range(len(points)):
                if i != j:
                    d = self.distance(points[i], points[j])
                    if d in dis:
                        dis[d] += 1
                    else:
                        dis[d] = 1
            for key in dis:
                if dis[key] > 1:
                    result += (dis[key] * (dis[key] - 1))
        return result

    def distance(self, p1, p2):
        return (p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1])

s = Solution()
print s.numberOfBoomerangs([[0,0],[1,0],[2,0],[3,0],[4,0]])