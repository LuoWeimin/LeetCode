#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        l = len(nums)
        sums = [0 for i in range(l)]
        sums[0] = nums[0]
        for i in range(1, l):
            sums[i] = sums[i - 1] + nums[i]
        if sums[l - 1] - sums[0] == 0:
            return 0
        for i in range(1, l):
            if sums[l - 1] - sums[i] == sums[i - 1]:
                return i
        return -1

s = Solution()
print s.pivotIndex([])
print s.pivotIndex([1])
print s.pivotIndex([1,2,3])
print s.pivotIndex([1, 7, 3, 6, 5, 6])
print s.pivotIndex([0,0,0,0,0])