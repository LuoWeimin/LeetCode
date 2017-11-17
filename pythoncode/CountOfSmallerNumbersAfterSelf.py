class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 1:
		return []
	b = [nums[-1]]
	c = [0]
	for i in range(len(nums) - 1):
		num = nums[len(nums) - 2 - i]
		mid = self.find(num, b)
		b.insert(mid, num)
		c.insert(0, mid)
	return c

    def find(self, num, b):
	left = 0
	right = len(b) - 1
	while (left <= right):
		mid = (left + right) / 2
		if b[mid] >= num:
			right = mid - 1
		else:
			left = mid + 1
	return left

s = Solution()
print s.countSmaller([5 , 2, 6, 1, 0, 7, 1, 5, 8, 2, 3, 4, 1, 2,1])
