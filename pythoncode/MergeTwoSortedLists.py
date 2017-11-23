# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
		return None
	elif l1 is None:
		return l2
	elif l2 is None:
		return l1
	else:
		l = ListNode(0)
		p = l
		while l1 is not None and l2 is not None:
			v1 = l1.val
			v2 = l2.val
			if v1 > v2:
				p.next = ListNode(v2)
				l2 = l2.next
			else:
				p.next = ListNode(v1)
				l1 = l1.next
			p = p.next
		if l1 is None:
			p.next = l2
		else:
			p.next = l1
	return l.next

s = Solution()
l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)
l1.next.next.next = ListNode(7)
l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)
l = s.mergeTwoLists(l1,l2)
while l is not None:
	print l.val
	l = l.next
