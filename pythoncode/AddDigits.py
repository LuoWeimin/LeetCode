#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            y = num % 9
            if y == 0:
                return 9
            else:
                return y
s = Solution()
print s.addDigits(111)