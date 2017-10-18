#!/usr/bin/python
# -*- coding: UTF-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        newHead = None
        newHeadHead = ListNode(0)
        newTail = None
        newTailHead = ListNode(0)
        while head is not None:
            if head.val < x:
                if newHead is None:
                    newHead = ListNode(head.val)
                    newHeadHead.next = newHead
                else:
                    temp = ListNode(head.val)
                    newHead.next = temp
                    newHead = temp
            else:
                if newTail is None:
                    newTail = ListNode(head.val)
                    newTailHead.next = newTail
                else:
                    temp = ListNode(head.val)
                    newTail.next = temp
                    newTail = temp
            head = head.next
        if newHead is None:
            return newTailHead.next
        newHead.next = newTailHead.next
        return newHeadHead.next

s = Solution()
head = ListNode(3)
# head.next = ListNode(4)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(2)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(2)
newHead = s.partition(head, 4)
while newHead is not None:
    print newHead.val
    newHead = newHead.next
