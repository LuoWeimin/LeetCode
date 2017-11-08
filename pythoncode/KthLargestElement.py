import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
	h = []
	for num in nums:
		heapq.heappush(h, num)
		if len(h) > k:
			heapq.heappop(h)
	return h[0]

s = Solution()
print s.findKthLargest([3,12,121,121,111,11,1, 123, 123123,1211,1231231], 4)
