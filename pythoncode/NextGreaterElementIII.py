#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n / 10 == 0:
            return -1
        else:
            digit = n % 10
            temp = n
            nums = []
            while temp != 0:
                num = temp % 10
                temp /= 10
                if num >= digit:
                    nums.append(num)
                    digit = num
                else:
                    nums.append(num)
                    result = str(temp)
                    nums = sorted(nums)
                    for i in nums:
                        if i > num:
                            result += str(i)
                            nums.remove(i)
                            break
                    for i in nums:
                        result += str(i)
                    if int(result) > pow(2, 31) - 1:
                        return -1
                    else:
                        return int(result)
            return -1
s = Solution()
print s.nextGreaterElement(2147483467)