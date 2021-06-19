# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
def calc_price(DIS: int, taxi_types: list) -> str:
    first_prices = [n[1] for n in taxi_types]
    remain_dis = [DIS - n[0] for n in taxi_types]
    add_prices = [n[3] for n in taxi_types]
    add_dis = [n[2] for n in taxi_types]
    
    def reach_goals(remain: int, add: int, add_price: int, sum: int = 0):
        if remain < 0 : return 0
        remain -= add
        sum += reach_goals(remain, add, add_price, sum) + add_price
        return sum
    
    prices = [first_prices[i] + reach_goals(remain_dis[i], add_dis[i], add_prices[i]) for i in range(N)]
    return f"{min(prices)} {max(prices)}"
N_DIS = input()
N, DIS = list(map(int, N_DIS.split()))
taxi_types = [list(map(int, input().split())) for _ in range(N)]

print(calc_price(DIS, taxi_types))

# sum = 0
# remain = 500

print(reach_goals(100000, 200, 100))


N_DIS = "3 600"
N, DIS = list(map(int, N_DIS.split()))

a = ["600 200 200 400","900 800 400 500", "200 200 200 300"]
taxi_types = [list(map(int, a[n].split())) for n in range(N)]

first_prices = [n[0] for n in taxi_types]
remain_dis = [DIS - n[1] for n in taxi_types]
add_prices = [n[2] for n in taxi_types]
add_dis = [n[3] for n in taxi_types]

# reach_goals(remain_dis[0], add_dis[0], add_prices[0])
print([first_prices[i] + reach_goals(remain_dis[i], add_dis[i], add_prices[i]) for i in range(N)])

