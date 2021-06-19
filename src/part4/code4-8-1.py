memo = []

def fibo(N: int) -> int:
    # base case
    if N == 0: return 0
    elif N == 1: return 1
    if memo[N] != -1: return memo[N]
    # recursibe
    memo[N] = fibo(N - 1) + fibo(N - 2)
    return memo[N]


if __name__ == "__main__":
    memo = [-1 for _ in range(7)]
    print(fibo(6))