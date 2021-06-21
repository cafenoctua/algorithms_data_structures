# 商品、クーポンA、クーポンBの数値を入力
N, A, B = list(map(int, input().split()))
print(f"{N} {A} {B}")

# 商品価格入力
prices = sorted(list(map(int, input().split())), reverse=True)
print(f"{prices}")

# クーポンBが使える商品


def liner_search(prices: int) -> int:
    L = 0
    R = len(prices)
    MID = int((R - L) / 2)
    while L <= R:
        if prices[MID] > 0:
            L += 1
            MID = int((R - L) / 2)
        elif prices[MID] < 0:
            R -= 1
            MID = int((R - L) / 2)
        else:
            return MID


prices_B = [0.05 * i - 100 if i >= 1000 else 0 for i in prices]

adopt_B = liner_search(prices_B)
if B < adopt_B:
    adopt_B = B
    B -= adopt_B
prices[:adopt_B] = [i * 0.95 for i in prices[:adopt_B]]
prices[adopt_B : adopt_B + A] = [i - 100 for i in prices[adopt_B : adopt_B + A]]
if B > 0:
    prices[adopt_B + A : adopt_B + A + B] = [
        i * 0.95 for i in prices[adopt_B + A : adopt_B + A + B]
    ]

print(sum(prices))
