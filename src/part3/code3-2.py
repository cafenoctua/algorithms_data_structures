if __name__ == "__main__":
    N: int = int(input())
    v: int = int(input())

    a: list = []
    for _ in range(N): a.append(int(input()))

    found_id: int = -1
    for i in range(N):
        if a[i] == v:
            found_id = i
            break

    print(found_id)