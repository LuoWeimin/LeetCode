#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        A = {}
        B = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                A[secret[i]] = A.get(secret[i], 0) + 1
                B[guess[i]] = B.get(guess[i], 0) + 1
        cows = 0
        for key in B:
            if key in A:
                cows += min(A[key], B[key])
        return str(bulls) + 'A' + str(cows) + 'B'

s = Solution()
print s.getHint("1123", "0111")