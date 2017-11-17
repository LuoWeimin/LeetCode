
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
	nums.sort()
	return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])

s = Solution()
print s.maximumProduct([-2, 1, 1])     
