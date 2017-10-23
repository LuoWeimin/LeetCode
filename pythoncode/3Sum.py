#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == -nums[i]:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                    left += 1
                elif s > -nums[i]:
                    right -= 1
                else:
                    left += 1
        return result

s = Solution()
print s.threeSum([-1,0,1,2,-1,-4])
