#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        s = nums[0:k]
        s.sort()
        r = [self.mid(s)]
        for i in range(k, len(nums)):
            s = self.delete(s, nums[i - k])
            s = self.insert(s, nums[i])
            r.append(self.mid(s))
        return r

    def mid(self, num):
        if len(num) % 2 == 1:
            return float(num[len(num) / 2])
        else:
            return (num[len(num) / 2 - 1] + num[len(num) / 2]) / 2.0

    def delete(self, num, n):
        left = 0
        right = len(num) - 1
        while left <= right:
            mid = (left + right) / 2
            if num[mid] == n:
                del num[mid]
                break
            elif num[mid] > n:
                right = mid - 1
            else:
                left = mid + 1
        return num

    def insert(self, num, n):
        left = 0
        right = len(num) - 1
        while left <= right:
            mid = (left + right) / 2
            if num[mid] >= n:
                right = mid - 1
            else:
                left = mid + 1
        num.insert(left, n)
        return num

s = Solution()
print s.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3)