from typing import List

class Solution:
    def runningSum(self, nums: List[int], i: int = 0) -> List[int]:
        # sum_list = []
        # sum_list.append(nums[0])
        # for i in range(1, len(nums)):
        #     sum_list.append(sum_list[i-1] + nums[i])
        # return sum_list
        i += 1
        if i >= len(nums): 
            return nums
        nums[i] += nums[i-1]
        return self.runningSum(nums, i)

solution = Solution()
print(solution.runningSum([1,2,3,4]))