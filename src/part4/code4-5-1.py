def fibo(N: int) -> int:
    # base case
    if N == 0: return 0
    elif N == 1: return 1

    # recursibe
    return fibo(N - 1) + fibo(N - 2)


if __name__ == "__main__":
    print(fibo(6))