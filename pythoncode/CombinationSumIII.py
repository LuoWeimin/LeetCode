#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.sum(k, n, [i for i in range(1, 10)])

    def sum(self, k, n, nums):
        if n < 0:
            return []
        if k == 1:
            for num in nums:
                if num == n:
                    return [[n]]
            return []
        else:
            res = []
            for i in range(len(nums)):
                temp = self.sum(k - 1, n - nums[i], nums[i + 1:])
                for ele in temp:
                    ele.append(nums[i])
                    res.append(ele)
            return res

s = Solution()
print s.combinationSum3(9, 45)