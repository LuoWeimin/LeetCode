#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        l = len(triangle) + 2
        path = [[sys.maxint for i in range(l)] for i in range(l)]
        path[0][0] = 0
        for i in range(1, l - 1):
            for j in range(1, i + 1):
                path[i][j] = min(path[i - 1][j - 1], path[i - 1][j]) + triangle[i - 1][j - 1]
        mp = sys.maxint
        for i in range(1, l):
            if mp > path[l - 2][i]:
                mp = path[l - 2][i]
        return mp

s = Solution()
print s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])