INF = 65535

class Solution:
    def tribonacci(self, N: int) -> int:
        memo = [INF for _ in range(N+1)]
        
        def calc_tribo(N: int) -> int:
            if N == 0: return 0
            elif N == 1: return 1
            elif N == 2 : return 1
            
            if memo[N] < INF: return memo[N]
            memo[N] = calc_tribo(N - 1) + calc_tribo(N - 2) + calc_tribo(N - 3)

            return calc_tribo(N - 1) + calc_tribo(N - 2) + calc_tribo(N - 3)
        
        return calc_tribo(N)

sol = Solution()
print(sol.tribonacci(36))