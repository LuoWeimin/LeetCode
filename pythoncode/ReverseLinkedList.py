#!/usr/bin/python
# -*- coding: UTF-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        p = None
        f = None
        while head.next is not None and head.next.next is not None:
            f = head.next
            s = f.next
            head.next = p
            f.next = head
            p = f
            head = s
        if head.next is not None:
            temp = head.next
            head.next = f
            temp.next = head
            return temp
        else:
            head.next = f
            return head

s = Solution()
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

head = s.reverseList(head)
while head is not None:
    print head.val
    head = head.next