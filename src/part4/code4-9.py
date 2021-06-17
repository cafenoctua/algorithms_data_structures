def func(i: int, w: int, a: list):
    # Base case
    if i == 0:
        if w == 0: return True
        else: return False
    
    # not select a[i - 1]
    if func(i - 1, w, a): return True

    # select a[i - 1]
    if func(i - 1, w - a[i - 1], a): return True

    return False

if __name__ == "__main__":
    N = 4
    W = 14
    a = [3,2,6,5]

    if func(N, W, a): print("Yes")
    else: print("No")