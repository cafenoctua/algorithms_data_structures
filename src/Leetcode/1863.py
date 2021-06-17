from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int], pre: int =0, i: int = -1) -> int:
        s = pre
        for j in range(i + 1, len(nums)):
            s += self.subsetXORSum(nums, pre ^ nums[j], j)
        return s


sol = Solution()
# print(sol.subsetXORSum([5,1,6]))
print(sol.subsetXORSum([2,4,4]))