#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        result = '1'
        while n > 1:
            s = result
            result = ''
            pre = s[0]
            count = 1
            for i in s[1:]:
                if i != pre:
                    result += (str(count) + pre)
                    pre = i
                    count = 1
                else:
                    count += 1
            result += (str(count) + pre)
            print result
            n -= 1
        return result

s = Solution()
print s.countAndSay(5)