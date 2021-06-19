INF: int = 20000000

if __name__ == "__main__":
    N: int = int(input())
    K: int = int(input())

    a: list = []
    b: list = []
    for _ in range(N): a.append(int(input()))
    for _ in range(N): b.append(int(input()))

    min_value: int = INF
    for i in range(N):
        for j in range(N):
            if a[i] + b[j] < K: continue
            if a[i] + b[j] < min_value: min_value = a[i] + b[j]

    print(min_value)