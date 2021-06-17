INF: int = 20000000

if __name__ == "__main__":
    N: int = int(input())

    a: list = []
    for _ in range(N): a.append(int(input()))

    min_value: int = INF
    for i in range(N):
        if a[i] < min_value: min_value = a[i]
    
    print(min_value)