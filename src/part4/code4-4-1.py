def GCD(x: int, y: int) -> int:
    if y == 0: return x
    return GCD(y, x%y)

if __name__ == "__main__":
    print(GCD(15, 51))