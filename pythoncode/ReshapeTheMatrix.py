#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums
        result = [[0 for i in range(c)] for i in range(r)]
        index = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                result[index / c][index % c] = nums[i][j]
                index += 1
        return result
s = Solution()
nums = [[1,2],[3,4]]
print s.matrixReshape(nums, 2, 4)