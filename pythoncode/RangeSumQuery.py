class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = [0 for _ in range(len(nums) + 1)]
        for i in range(0, len(nums)):
            self.sums[i] = self.sums[i - 1] + nums[i]
        print self.sums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j] - self.sums[i - 1]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
print obj.sumRange(0,2)
print obj.sumRange(2,5)
print obj.sumRange(0,5)

