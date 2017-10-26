#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = sorted(nums)[len(nums) / 2]
        return sum(abs(num - median) for num in nums)

s = Solution()
print s.minMoves2([1, 1, 2, 2, 3, 3, 3, 3, 3])
