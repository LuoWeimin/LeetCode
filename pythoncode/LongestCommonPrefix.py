#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ''
        else:
            cp = strs[0]
            for s in strs[1:]:
                cp = self.compareTwoString(cp,  s)
        return cp

    def compareTwoString(self, str1, str2):
        if not str2 or str2 == '' or not str1 or str1 == '':
            return ''
        index = 0
        while index < len(str1) and index < len(str2):
            if str1[index] == str2[index]:
                index += 1
            else:
                break
        return str1[:index]

s = Solution()
print s.longestCommonPrefix(['aaa', 'bbb','ccc'])
print s.longestCommonPrefix([])
print s.longestCommonPrefix([''])
print s.longestCommonPrefix(['', 'bbb','ccc'])
print s.longestCommonPrefix(['bb', 'bbb','bbbb'])
print s.longestCommonPrefix(['pre-', 'pre-va','pre-zs'])