#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # count = [0 for _ in range(n + 1)]
        # for i in range(1, n + 1):
        #     j = 1
        #     while i * j < n + 1:
        #         count[i * j] += 1
        #         j += 1
        # result = 0
        # for _ in count:
        #     if _ % 2 == 1:
        #         result += 1
        # return result
        return int(math.floor(math.sqrt(n)))

s = Solution()
for i in range(100):
    print s.bulbSwitch(i)