def fibo(N: int) -> int:
    F = []
    F.append(0)
    F.append(1)
    for i in range(2, N):
        F.append(F[i - 1] + F[i - 2])
        print(f"{N}項目目: {F[i]}")
    return F[i]
if __name__ == "__main__":
    print(fibo(50))