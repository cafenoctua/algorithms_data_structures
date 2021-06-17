def fibo(N: int) -> int:
    # debug
    print(f"fibo({N})を呼び出した")
    # base case
    if N == 0: return 0
    elif N == 1: return 1


    result = fibo(N - 1) + fibo(N - 2)

    print(f"{N}項目目 = {result}")
    return result

if __name__ == "__main__":
    print(fibo(6))