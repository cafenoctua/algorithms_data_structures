def GCD(m: int, n: int) -> int:
    # base case
    if n == 0: return m
    
    # call
    return GCD(n, m % n)

if __name__ == "__main__":
    print(GCD(51, 15))
    print(GCD(15, 51))
    