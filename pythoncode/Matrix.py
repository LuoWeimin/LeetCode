#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        step = [[sys.maxint for i in range(len(matrix[0]) + 2)] for i in range(len(matrix) + 2)]
        flag = [[False for i in range(len(matrix[0]) + 2)] for i in range(len(matrix) + 2)]
        for i in range(len(matrix[0]) + 2):
            flag[0][i] = True
            flag[len(step) - 1][i] = True
        for i in range(len(matrix) + 2):
            flag[i][0] = True
            flag[i][len(step[0]) - 1] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    step[i + 1][j + 1] = 0
                    flag[i + 1][j + 1] = True
        c = False
        s = 0
        while not c:
            c = True
            for i in range(1, len(step) - 1):
                for j in range(1, len(step[i]) - 1):
                    if step[i][j] == s:
                        c = False
                        if not flag[i - 1][j]:
                            step[i - 1][j] = s + 1
                            flag[i - 1][j] = True
                        if not flag[i + 1][j]:
                            step[i + 1][j] = s + 1
                            flag[i + 1][j] = True
                        if not flag[i][j - 1]:
                            step[i][j - 1] = s + 1
                            flag[i][j - 1] = True
                        if not flag[i][j + 1]:
                            step[i][j + 1] = s + 1
                            flag[i][j + 1] = True
            s += 1
        return [i[1:len(i) - 1] for i in step[1:len(step) - 1]]

s = Solution()
print s.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])