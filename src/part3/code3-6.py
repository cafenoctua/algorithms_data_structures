if __name__ == "__main__":
    N: int = int(input())
    W: int = int(input())

    a = []
    for _ in range(N): a.append(int(input()))

    # bitは2^N通りの部分集合全体を動きます
    exist: bool = False
    for bit in range(1 << N):
        sum: int = 0 # 部分集合が含まれる要素の和
        for i in range(N):
            # i番目に要素a[i]が部分集合に含まれているかどうか
            if bit & (1 << i):
                sum += a[i]

        if sum == W: exist = True

    if exist: print("Yes")
    else: print("No")