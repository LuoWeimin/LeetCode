#!/usr/bin/python
# -*- coding: UTF-8 -*-
import heapq
import math


class Solution(object):
    def findKthNumber(self, m, n, k):
        def enough(x):
            return sum(min(x / i, n) for i in xrange(1, m + 1)) >= k

        lo, hi = 1, m * n
        while lo < hi:
            mi = (lo + hi) / 2
            if not enough(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo

s = Solution()
# for i in range(1, 100):
    # print i, s.kthNumber(30000, 30000, i, -1)
print s.findKthNumber(2, 4, 8)
