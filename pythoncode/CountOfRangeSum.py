#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sum = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
                sum[i + 1] = nums[i] + sum[i]
        return self.countWhileMergeSort(sum, 0, len(nums) + 1, lower, upper)

    def countWhileMergeSort(self, sums, start, end, lower, upper):
        if end - start <= 1:
            return 0
        mid = (start + end) / 2
        count = self.countWhileMergeSort(sums, start, mid, lower, upper) + \
                self.countWhileMergeSort(sums, mid, end, lower, upper)
        j = k = t = mid
        cache = [0 for _ in range(end - start)]
        r = 0
        for i in range(start, mid):
            while k < end and sums[k] - sums[i] < lower:
                k += 1
            while j < end and sums[j] - sums[i] <= upper:
                j += 1
            while t < end and sums[t] < sums[i]:
                cache[r] = sums[t]
                r += 1
                t += 1
            cache[r] = sums[i]
            count += j - k
            r += 1
        for i in range(0, t - start):
            sums[i + start] = cache[i]
        return count

s = Solution()
print s.countRangeSum([-2, 5, -1], -2, 2)

