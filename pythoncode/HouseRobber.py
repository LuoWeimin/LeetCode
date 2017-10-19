#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        mb = [0 for _ in range(len(nums))]
        mb[0] = nums[0]
        mb[1] = max(nums[0], nums[1])
        flag = mb[1] == nums[1]
        for i in range(2, len(nums)):
            if flag:
                mb[i] = max(mb[i - 1], mb[i - 2] + nums[i])
                if mb[i] == mb[i - 1]:
                    flag = False
                else:
                    flag = True
            else:
                mb[i] = mb[i - 1] + nums[i]
                flag = True
            print mb[i]
        return mb[-1]


s = Solution()
print s.rob([2, 2, 100, 4, 5, 6, 7, 1000, 10, 12, 12])
print s.rob([2, 1, 1, 2])
