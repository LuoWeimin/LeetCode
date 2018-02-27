class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 + l2 > k:
            mi1 = -1
            mx1 = -1
            for n in range(l1):
                if mx1 < nums1[n] and l1 - n - 1 + l2 >= k - 1:
                    mx1 = nums1[n]
                    mi1 = n
            mi2 = -1
            mx2 = -1
            for n in range(l2):
                if mx2 < nums2[n] and l2 - n - 1 + l1 >= k - 1:
                    mx2 = nums2[n]
                    mi2 = n
            if mx1 > mx2:
                r1 = [mx1]
                r1.extend(self.maxNumber(nums1[mi1 + 1:], nums2, k - 1))
                return r1
            elif mx2 > mx1:
                r2 = [mx2]
                r2.extend(self.maxNumber(nums1, nums2[mi2 + 1:], k - 1))
                return r2
            else:
                r1 = [mx1]
                r1.extend(self.maxNumber(nums1[mi1 + 1:], nums2, k - 1))
                r2 = [mx2]
                r2.extend(self.maxNumber(nums1, nums2[mi2 + 1:], k - 1))
                return max(r1, r2)
        else:
            res = []
            if not nums1:
                res.extend(nums2)
            elif not nums2:
                res.extend(nums1)
            else:
                if nums1[0] > nums2[0]:
                    res.append(nums1[0])
                    res.extend(self.maxNumber(nums1[1:], nums2, k - 1))
                elif nums1[0] < nums2[0]:
                    res.append(nums2[0])
                    res.extend(self.maxNumber(nums1, nums2[1:], k - 1))
                else:
                    r1 = [nums1[0]]
                    r1.extend(self.maxNumber(nums1[1:], nums2, k - 1))
                    r2 = [nums2[0]]
                    r2.extend(self.maxNumber(nums1, nums2[1:], k - 1))
                    return max(r1, r2)
            return res

    def maxNumber1(self, nums1, nums2, k):

        def prep(nums, k):
            drop = len(nums) - k
            out = []
            for num in nums:
                while drop and out and out[-1] < num:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in a + b]

        return max(merge(prep(nums1, i), prep(nums2, k - i))
                   for i in range(k + 1)
                   if i <= len(nums1) and k - i <= len(nums2))

s = Solution()
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
# nums1 = [6, 0, 4]
# nums2 = [6, 7]
# k = 5
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# nums1 = [6,7,5]
# nums2 = [4,8,1]
# k = 3
print s.maxNumber1(nums1, nums2, k)
