#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        maxPath = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        max = 0
        for i in range(len(maxPath)):
            for j in range(len(maxPath[0])):
                maxPath[i][j] = self.path(matrix, i, j, maxPath)
                if max < maxPath[i][j]:
                    max = maxPath[i][j]
        return max

    def path(self, matrix, x, y, maxPath):
        if x < 0 or x > len(matrix) - 1 or y < 0 or y > len(matrix[x]) - 1:
            return -sys.maxint
        if maxPath[x][y] != 0:
            return maxPath[x][y]
        max = 0
        if matrix[x][y] > self.getMatrixValue(matrix, x - 1, y):
            temp = self.path(matrix, x - 1, y, maxPath)
            if max < temp:
                max = temp
        if matrix[x][y] > self.getMatrixValue(matrix, x, y - 1):
            temp = self.path(matrix, x, y - 1, maxPath)
            if max < temp:
                max = temp
        if matrix[x][y] > self.getMatrixValue(matrix, x, y + 1):
            temp = self.path(matrix, x, y + 1, maxPath)
            if max < temp:
                max = temp
        if matrix[x][y] > self.getMatrixValue(matrix, x + 1, y):
            temp = self.path(matrix, x + 1, y, maxPath)
            if max < temp:
                max = temp
        maxPath[x][y] = max + 1
        return max + 1

    def getMatrixValue(self, matrix, x, y):
        if x < 0 or x > len(matrix) - 1 or y < 0 or y > len(matrix[x]) - 1:
            return sys.maxint
        else:
            return matrix[x][y]

s = Solution()
print s.longestIncreasingPath(
  [
  [4,5]])