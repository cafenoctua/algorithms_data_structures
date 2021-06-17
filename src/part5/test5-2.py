if __name__ == "__main__":
    N = 5
    W = 4
    a = [2,5,1,6,7]

    
    dp = [[False for _ in range(W+1)] for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(W):
            if not(dp[i][j]): continue
            dp[i+1][j] = True
            if j+a[i] <= W: dp[i+1][j+a[i]] = True
    if dp[N][W]: print("Yes")
    else: print("No")

    