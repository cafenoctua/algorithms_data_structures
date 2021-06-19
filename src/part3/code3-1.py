if __name__ == "__main__":
    N, v = int(input()), int(input())

    a = []
    for _ in range(N): a.append(int(input()))

    exist = False
    for i in range(N):
        if a[i] == v:
            exist = True

    if exist:
        print("Yes")
    else:
        print("No")