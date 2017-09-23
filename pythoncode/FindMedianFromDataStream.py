#!/usr/bin/python
# -*- coding: UTF-8 -*-


# class Tree(object):
#     def __init__(self, val, left, right):
#         self.data = val
#         self.left = left
#         self.right = right
#
#
# class MedianFinder(object):
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.mid = Tree(-1, None, None)
#         self.length = 0
#         self.ll = 0
#         self.rl = 0
#
#     def addNum(self, num):
#         """
#         :type num: int
#         :rtype: void
#         """
#         if self.length == 0:
#             self.mid.left = Tree(num, None, None)
#         else:
#             if self.mid.left.data > num:
#                 current = self.mid.left
#                 while current.left is not None and current.left.data > num:
#                     current = current.left
#                 if current.left is None:
#                     current.left = Tree(num, None, None)
#                 else:
#                     temp = Tree(num, current.left, None)
#                     current.left = temp
#                 self.ll += 1
#             else:
#                 current = self.mid.left
#                 while current.right is not None and current.right.data < num:
#                     current = current.right
#                 if current.right is None:
#                     current.right = Tree(num, None, None)
#                 else:
#                     temp = Tree(num, None, current.right)
#                     current.right = temp
#                 self.rl += 1
#             if self.ll > self.rl + 1:
#                 current = self.mid.left
#                 current.left.right = current
#                 self.mid.left = current.left
#                 current.left = None
#                 self.ll -= 1
#                 self.rl += 1
#             elif self.rl > self.ll + 1:
#                 current = self.mid.left
#                 current.right.left = current
#                 self.mid.left = current.right
#                 current.right = None
#                 self.rl -= 1
#                 self.ll += 1
#         self.length += 1
#
#     def findMedian(self):
#         """
#         :rtype: float
#         """
#         if self.ll == self.rl:
#             return self.mid.left.data
#         elif self.ll > self.rl:
#             return (self.mid.left.data + self.mid.left.left.data) / 2.0
#         else:
#             return (self.mid.left.data + self.mid.left.right.data) / 2.0

import heapq


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.maxHeap, -num)
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        else:
            return -self.maxHeap[0]

s = MedianFinder()
s.addNum(6)
print s.findMedian()
s.addNum(10)
print s.findMedian()
s.addNum(2)
print s.findMedian()
s.addNum(6)
print s.findMedian()
s.addNum(5)
print s.findMedian()
s.addNum(0)
print s.findMedian()
s.addNum(6)
print s.findMedian()
s.addNum(3)
print s.findMedian()
s.addNum(1)
print s.findMedian()
s.addNum(0)
print s.findMedian()
s.addNum(0)
print s.findMedian()