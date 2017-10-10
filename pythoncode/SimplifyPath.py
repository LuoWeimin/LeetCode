#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if path == '':
            return ''
        dir = []
        temp = ''
        for s in path:
            if s == '/':
                if temp == '':
                    temp = ''
                elif temp == '.':
                    temp = ''
                elif temp == '..':
                    if len(dir) != 0:
                        dir.pop(-1)
                    temp = ''
                else:
                    dir.append(temp)
                    temp = ''
            else:
                temp += s
        if temp != '':
            if temp == '.':
                temp = ''
            elif temp == '..':
                if len(dir) != 0:
                    dir.pop(-1)
            else:
                dir.append(temp)
        rs = ''
        for d in dir:
            rs += '/' + d
        if rs == '':
            return '/'
        return rs

s = Solution()
print s.simplifyPath('/Z/Iyy/HSyT/ItVqc/.././//Z/.././.././../a/gK/../ZurH///x/../////././../..')
print s.simplifyPath("/a/./b/../../c/")
