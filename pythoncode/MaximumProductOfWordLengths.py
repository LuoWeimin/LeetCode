#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        w = []
        for word in words:
            temp = 0
            for c in word:
                temp |= (1 << (ord(c) - ord('a')))
            w.append(temp)
        max = 0
        for i in range(len(w)):
            for j in range(i + 1, len(w)):
                if w[i] & w[j] == 0:
                    size = len(words[i]) * len(words[j])
                    if max < size:
                        max = size
        return max

s = Solution()
print s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
