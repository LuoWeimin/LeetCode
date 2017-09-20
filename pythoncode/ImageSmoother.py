#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        result = [[0 for i in range(len(M[0]))] for i in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[i])):
                left = j - 1
                right = j + 1
                up = i - 1
                down = i + 1
                if i == 0:
                    up = 0
                if i == len(M) - 1:
                    down = len(M) - 1

                if j == 0:
                    left = 0
                if j == len(M[0]) - 1:
                    right = len(M[0]) - 1
                sum = 0
                for m in range(up, down + 1):
                    for n in range(left, right + 1):
                        sum += M[m][n]
                result[i][j] = sum / ((down - up + 1) * (right - left + 1))
        return result

s = Solution()
print s.imageSmoother([[1,1,1],
 [1,0,1],
 [1,1,1]])


