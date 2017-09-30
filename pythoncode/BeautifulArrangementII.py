#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = [0 for _ in range(n)]
        i = 0
        r = n
        l = 1
        while l <= r:
            if k > 1:
                if k % 2 != 0:
                    res[i] = l
                    l += 1
                else:
                    res[i] = r
                    r -= 1
                k -= 1
            else:
                res[i] = l
                l += 1
            i += 1
        return res

s = Solution()
print s.constructArray(4, 1)
