INF = 20000000

if __name__ == "__main__":
    N = 7
    h = [2, 9, 4, 5, 1, 6, 10]
    dp = []
    dp.append(0)

    for i in range(1, N):
        if i == 1: dp.append(abs(h[i] - h[i-1]))
        else: dp.append(min(dp[i - 1] + abs(h[i] - h[i-1]), dp[i - 2] + abs(h[i] - h[i - 2])))

    print(dp)