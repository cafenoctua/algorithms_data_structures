from typing import List
from collections import Counter

class Solution:
    def countBits(self, n: int) -> List[int]:
        # s = []
        # for i in range(n+1):
        #     s.append(sum(list(map(int, Counter(bin(i)[2:]).elements()))))
        
        # return s
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i&1)
        return dp

sol = Solution()
print(sol.countBits(5))