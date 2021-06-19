INF = 20000000

def chmin(a, b):
    if a > b: return b
    return a

if __name__ == "__main__":
    N = 7
    h = [2, 9, 4, 5, 1, 6, 10]
    dp = [INF for _ in range(N)]
    dp[0] = 0
    for i in range(1, N):
        dp[i] = chmin(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]))
        if i > 1: dp[i] = chmin(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]))

    print(dp)