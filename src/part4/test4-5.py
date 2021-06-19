N = 575
counter = 0
def myfunc(N: int):
    div10 = 10
    i = 0
    counter = 0
    while N  // (div10 ** i) > 0:
        div = N // (div10 ** i) - N // (div10 ** (i+1)) * 10
        if div == 7 or div == 5 or div == 3: counter += 1
        i += 1

    return counter

def func(N: int, cur: int, use: int):
    global counter
    if cur > N: return;
    if use == 0b111: counter += 1

    func(N, cur * 10 + 7, use | 0b001)
    func(N, cur * 10 + 5, use | 0b010)
    func(N, cur * 10 + 3, use | 0b100)

if __name__ == "__main__":
    # myfunc(N)
    counter = 0
    func(N, 0, 0)
    print(counter)