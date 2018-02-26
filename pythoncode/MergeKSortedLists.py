from Queue import PriorityQueue


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize() > 0:
            curr.next = q.get()[1]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, curr.next))
        return dummy.next


l1 = ListNode(1)
l1.next = ListNode(2)
l2 = ListNode(2)
l2.next = ListNode(3)
l3 = ListNode(0)
l3.next = ListNode(1)
l4 = ListNode(5)
l4.next = ListNode(6)
lists = [l1, l2, l3, l4]
s = Solution()
r = s.mergeKLists(lists)
while r:
    print r.val
    r = r.next
