#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = len(s)
        i = 0
        r = ''
        while True:
            if l - i < k:
                j = l - 1
                while j >= i:
                    r += s[j]
                    j -= 1
                return r
            elif l - i < 2 * k:
                j = i + k - 1
                while j >= i:
                    r += s[j]
                    j -= 1
                j = i + k
                while j < l:
                    r += s[j]
                    j += 1
                return r
            else:
                j = i + k - 1
                while j >= i:
                    r += s[j]
                    j -= 1
                j = i + k
                while j < i + 2 * k:
                    r += s[j]
                    j += 1
                i += 2 * k

s = Solution()
print s.reverseStr("abcdefghi", 2)