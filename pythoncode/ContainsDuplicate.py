#!/usr/bin/python
# -*- coding: UTF-8 -*-
import collections


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False
        c = collections.Counter(nums)
        for key in c:
            if c[key] > 1:
                return True
        return False

s = Solution()
print s.containsDuplicate([0])
