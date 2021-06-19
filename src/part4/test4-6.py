memo: list = [[]]

def func(i: int, w: int, a: list):
    global memo
    # Base case
    if i == 0:
        if w == 0: return True
        else: return False
    
    if memo[i][w] != -1: return memo[i][w]
    # not select a[i - 1]
    if func(i - 1, w, a): 
        memo[i][w] = 1  
        return memo[i][w]

    # select a[i - 1]
    if func(i - 1, w - a[i - 1], a): 
        memo[i][w] = 1  
        return memo[i][w]

    memo[i][w] = 0
    return memo[i][w]

if __name__ == "__main__":
    # global memo
    N = 4
    W = 14
    a = [3,2,6,5]
    memo = [[-1 for _ in range(W+1)] for _ in range(N+1)]
    if func(N, W, a): print("Yes")
    else: print("No")