#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Node(object):
    def __init__(self, val, p=0):
        self.data = val
        self.next = p


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = Node(-1)
        self.left_mid = Node()
        self.right_mid = Node()
        self.length = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.length == 0:
            node = Node(num)
            self.head.next = node
            self.left_mid = self.head.next
            self.right_mid = self.head.next
            self.length += 1
        else:
            node = Node(num)
            p = Node(self.head)
            while p.next !


    def findMedian(self):
        """
        :rtype: float
        """
        return (self.left_mid.data + self.right_mid.data)/2
