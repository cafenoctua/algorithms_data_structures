memo: list = []

def fibo(N: int) -> int:
    # Base case
    if N == 0: return 0
    elif N == 1: return 1

    # Check memoes
    if memo[N] != -1: return memo[N]

    # recall def and memo
    memo[N] = fibo(N - 1) + fibo(N - 2)
    return memo[N]


if __name__ == "__main__":
    N = 50
    memo = [-1 for _ in range(N)]

    fibo(49)
    print([i for i in memo])