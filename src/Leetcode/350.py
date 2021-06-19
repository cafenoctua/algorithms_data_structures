from typing import List
import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums_l = iter(nums1) if len(nums1) >= len(nums2) else iter(nums2)
        # nums_s = nums1 if len(nums1) < len(nums2) else nums2
        # nums = []
        # for i in range(len(nums_s)):
        #     if nums_s[i] in nums_l:
        #         nums.append(nums_s[i])
        # nums_l = nums1 if len(nums1) >= len(nums2) else nums2
        # nums_s = nums1 if len(nums1) < len(nums2) else nums2
        # nums = []
        # for n in nums_s:
        #     if n in nums_l:
        #         nums.append(n)
        #         nums_l.remove(n)
        # return nums
        
        a, b = map(collections.Counter, (nums1, nums2))
        return list((a & b).elements())

        


sol = Solution()
print(sol.intersect([1,2,2,1], [2,2]))
print(sol.intersect([4,9,5], [9,4,9,8,4]))
print(sol.intersect([2,9,2], [2,4,9,8,2]))

