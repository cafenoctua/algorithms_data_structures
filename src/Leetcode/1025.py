INF = 1 << 50
class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False for i in range(n+1)]
        dp[0] = True
        if n <= 1:
            return dp[n]
        for i in range(2, n+1):
            for j in range(1, n//2 + 1):
                if i % j == 0 and (not dp[i - j]):
                    dp[i] = True
                    break

        return dp[n]

sol = Solution()
print(sol.divisorGame(30))