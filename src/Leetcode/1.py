from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return [hash_table[nums[i]], i]
            else:
                hash_table[target - nums[i]] = i
        
sol = Solution()
# print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([-1,-2,-3,-4, -5], -8))