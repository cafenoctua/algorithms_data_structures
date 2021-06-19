from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1
        n = len(nums)
        r = n-1
        l = 0
        c = (r + l) // 2
        while l <= r:
            c = (r + l) // 2
            if nums[c] == target: return c
            elif nums[c] < target: l = c + 1
            else: r = c - 1
        return -1

sol = Solution()
print(sol.search([-1,0,3,5,9,12], 9))
print(sol.search([-1,0,3,5,9,12], 2))