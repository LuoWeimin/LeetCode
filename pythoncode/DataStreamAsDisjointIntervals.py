#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class SummaryRanges(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_steam = list()

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        start = -1
        end = -1
        index = 0
        for i in range(len(self.data_steam)):
            if val < self.data_steam[i].start - 1:
                break
            elif val == self.data_steam[i].start - 1:
                end = i
            elif val == self.data_steam[i].end + 1:
                start = i
            elif self.data_steam[i].start <= val <= self.data_steam[i].end:
                return
            index += 1
        if start != -1 and end != -1:
            self.data_steam[start] = Interval(self.data_steam[start].start, self.data_steam[end].end)
            self.data_steam.remove(self.data_steam[end])
        elif start != -1:
            self.data_steam[start] = Interval(self.data_steam[start].start, val)
        elif end != -1:
            self.data_steam[end] = Interval(val, self.data_steam[end].end)
        else:
            self.data_steam.insert(index, Interval(val, val))

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.data_steam

s = SummaryRanges()
for i in range(100000):
    s.addNum(random.randint(1, 10000))

for _ in s.getIntervals():
    print _.start, _.end
