#!/usr/bin/python
# -*- coding: UTF-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = 0
        p = ListNode(0)
        p.next = head
        while p.next:
            l += 1
            p = p.next
        p = ListNode(0)
        p.next = head
        if l == n:
            return head.next
        while l - n:
            p = p.next
            n += 1
        d = p.next.next
        p.next = d
        return head

l = ListNode(0)
l.next = ListNode(1)
l.next.next = ListNode(2)
l.next.next.next = ListNode(3)
l.next.next.next.next = ListNode(4)

s = Solution()
l = s.removeNthFromEnd(l, 1)
while l:
    print l.val
    l = l.next
