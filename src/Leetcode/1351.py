from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]):
        # Return if grid have only 1 number
        if len(grid) == 0:
            return 0
        if len(grid) == 1 and type(grid[0]) == int:
            return 1 if grid[0] < 0 else 0
        # if len(grid) == 1 and len(grid[0]) == 1:
        #     return 1 if grid[0] < 0 else 0
        grid = grid if len(grid) > 1 else grid[0]
        N = len(grid)
        L = 0
        R = N
        MID = int(R / 2)

        # split list
        # num negative function
        num_negative = self.countNegatives(grid[L:MID]) + self.countNegatives(
            grid[MID:R]
        )

        return num_negative


sol = Solution()
# grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
# print(sol.countNegatives(grid))
grid = [[-1]]
print(sol.countNegatives(grid))
