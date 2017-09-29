#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = [0 for _ in range(26)]
        for i in s:
            count[ord(i) - ord('a')] += 1
        for i in range(len(s)):
            if count[ord(s[i]) - ord('a')] == 1:
                return i
        return -1

s = Solution()
print s.firstUniqChar('ccaaaabb')