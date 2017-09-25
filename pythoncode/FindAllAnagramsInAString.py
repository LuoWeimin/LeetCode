#!/usr/bin/python
# -*- coding: UTF-8 -*-

import copy


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        char_count_p = [0 for i in range(26)]
        for i in p:
            char_count_p[ord(i) - ord('a')] += 1

        char_count_s = [0 for i in range(26)]
        index = []
        length = 0
        for i in range(len(s)):
            if length >= len(p):
                char_count_s[ord(s[i - len(p)]) - ord('a')] -= 1
            char_count_s[ord(s[i]) - ord('a')] += 1
            if self.compare(char_count_s, char_count_p):
                index.append(i - len(p) + 1)
            length += 1
        return index

    def compare(self, array1, array2):
        for i in range(len(array1)):
            if array1 != array2:
                return False
        return True


s = Solution()
print s.findAnagrams('', '')