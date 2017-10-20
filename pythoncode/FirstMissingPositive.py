#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array = {}
        for num in nums:
            if num > 0:
                array[num] = 1
        flag = 0
        for key in array:
            flag += 1 << (key - 1)
        count = 0
        while flag > 0:
            count += 1
            if flag % 2 != 1:
                return count
            flag >>= 1
        return count + 1

s = Solution()
print s.firstMissingPositive([1, 2, 3, 4, 5])