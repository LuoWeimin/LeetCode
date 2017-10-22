#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        diff = []
        for i in range(1, len(A)):
            diff.append(A[i] - A[i - 1])
        last = diff[0]
        count = 1
        res = 0
        for i in range(1, len(diff)):
            if diff[i] == last:
                count += 1
            else:
                last = diff[i]
                res += (count * (count - 1)) / 2
                count = 1
        res += (count * (count - 1)) / 2
        return res

s = Solution()
print s.numberOfArithmeticSlices([7, 7])