#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -1
        else:
            left = 0
            right = x
            while 1:
                if right - left == 1:
                    if right * right == x:
                        return right
                    return left
                mid = (left + right) / 2
                square = mid * mid
                if square == x:
                    return mid
                elif square < x:
                    left = mid
                else:
                    right = mid

s = Solution()
print s.mySqrt(0)
print s.mySqrt(1)
print s.mySqrt(4)
print s.mySqrt(10086)