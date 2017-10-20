#!/usr/bin/python
# -*- coding: UTF-8 -*-
import heapq


class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count and self.word == other.word


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = {}
        ch = []
        for word in words:
            count[word] = count.get(word, 0) + 1
        for key in count:
            heapq.heappush(ch, Element(count[key], key))
            if len(ch) > k:
                heapq.heappop(ch)
        ch.sort()
        return [ch[item].word for item in range(len(ch) - 1, -1, -1)]


s = Solution()
# print s.topKFrequent(["i", "love", "leetcode", "i", "love", "code", "a", "m", "b"], 4)
print s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
