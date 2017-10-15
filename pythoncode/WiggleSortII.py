#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        half = len(nums[::2]) - 1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]

s = Solution()
s.wiggleSort([1,1,1,4,5,6])