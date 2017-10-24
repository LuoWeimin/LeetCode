#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        ms = []
        num = 1
        ms.append(num)
        num = 2 if num == 1 else 1
        count = 1
        ms.append(num)
        ms.append(num)
        slow = 2
        while len(ms) < n:
            num = 2 if num == 1 else 1
            for i in range(ms[slow]):
                ms.append(num)
            if num == 1:
                count += ms[slow]
            slow += 1
        count -= len(ms) - n if num == 1 else 0
        return count
s = Solution()
for i in range(1, 20):
    print s.magicalString(i)