#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2 == 1:
            return False
        else:
            s /= 2
            dp = [False for i in range(s + 1)]
            dp[0] = True

            for num in nums:
                i = s
                while i > 0:
                    if i >= num:
                        dp[i] = dp[i] or dp[i - num]
                    i -= 1
            return dp[s]

s = Solution()
print s.canPartition([1, 5, 5, 11])