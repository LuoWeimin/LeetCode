class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = [0 for _ in range(nums[len(nums) - 1] - nums[0] + 1 + 3)]
        appendfreq = [0 for _ in range(nums[len(nums) - 1] - nums[0] + 1 + 3)]
        for num in nums:
            freq[num - nums[0]] += 1
        for num in nums:
            index = num - nums[0]
            if freq[index] == 0:
                continue
            elif appendfreq[index] > 0:
                appendfreq[index] -= 1
                appendfreq[index + 1] += 1
            elif freq[index + 1] > 0 and freq[index + 2] > 0:
                freq[index + 1] -= 1
                freq[index + 2] -= 1
                appendfreq[index + 3] += 1
            else:
                return False
            freq[index] -= 1
            print freq, appendfreq
        return True

s = Solution()
print s.isPossible([1,2,3,4,4,5])
# print s.isPossible([1,1,1,2,2,3])
# print s.isPossible([1,2,3,4,5,7,8,9])
# print s.isPossible([1,2,3,3,3,4,4,5])
# print s.isPossible([1,2,3,3,4,5,5,6,7,7,7,8,8,9,9])
