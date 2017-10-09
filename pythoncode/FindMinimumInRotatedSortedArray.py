#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums[0], nums[1])
        mid = left + (right - left) / 2
        if nums[left] == nums[mid] and nums[mid] == nums[right]:
            return min(self.findMin(nums[0: mid]), self.findMin(nums[mid:]))

        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = left + (right - left) / 2
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

s = Solution()
print s.findMin([1,0])
print s.findMin([5,5,5,5,5,5,6,7,7,7,7,7,0,0,0,0,0,1,1,1,1,1,2,3,4,5,5,5,5,5,5,5])
print s.findMin([10,1,10,10,10])