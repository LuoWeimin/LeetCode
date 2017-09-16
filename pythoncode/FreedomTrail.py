#!/usr/bin/python

import sys

class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        step = [[0 for i in range(len(ring))] for i in range(len(key))]
        list = [[] for i in range(128)]
        for i in range(len(ring)):
            list[ord(ring[i])].append(i)

        first_char = key[0]
        length = len(ring)
        for i in list[ord(first_char)]:
            step[0][i] = min(i, length - i)

        last = first_char
        for i in range(1, len(key)):
            current = key[i]
            for j in list[ord(current)]:
                step[i][j] = sys.maxint
                for k in list[ord(last)]:
                    dis = abs(j - k)
                    step[i][j] = min(step[i][j], step[i - 1][k] + min(dis, length - dis))
            last = current
        min_dis = sys.maxint
        for i in list[ord(key[-1])]:
            if min_dis > step[len(key) - 1][i]:
                min_dis = step[len(key) - 1][i]
        return min_dis + len(key)

s = Solution()
print s.findRotateSteps('godding', 'godding')