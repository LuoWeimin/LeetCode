#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution(object):
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        str = ''
        num = 1
        for i in range(len(s)):
            if s[i] == '0':
                if i == 0:
                    return 0
                elif int(s[i - 1]) > '2':
                    return 0
                else:
                    str += s[i]
                    num *= self.easy(str)
                    str = ''
            elif s[i] < '3':
                str += s[i]
            else:
                if str != '':
                    str += s[i]
                    num *= self.easy(str)
                    str = ''
        if str != '':
            num *= self.easy(str)
        return num

    def easy(self, s):
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            if int(s) != 0:
                return 1
            else:
                return 0
        elif len(s) == 2:
            if int(s) == 0 or int(s[0]) == 0:
                return 0
            elif int(s[1]) == 0 and int(s[0]) < 3:
                return 1
            elif 27 > int(s) > 0:
                return 2
            else:
                return self.numDecodings(s[1])
        else:
            if int(s[0:2]) == 0 or int(s[0]) == 0:
                return 0
            elif int(s[1]) == 0 and int(s[0]) < 3:
                return self.numDecodings(s[2:])
            elif 27 > int(s[0:2]) > 0:
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            else:
                return self.numDecodings(s[1:])

s = Solution()
print s.numDecodings("0")