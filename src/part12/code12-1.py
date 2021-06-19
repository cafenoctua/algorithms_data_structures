def InsertionSort(data: list) -> list:
    N = len(data)
    for i in range(1, N):
        v = data[i]
        j = i
        while j > 0:
            # vが小さければ入れ替える
            if data[j-1] > v:
                data[j] = data[j-1]
            else:
                break # 比較する数値がv以下になったら止める
            j -= 1
        # vの適切な場所jが設定されているのでそこにおこかれる
        data[j] = v
    return data

if __name__ == "__main__":
    # # 要素数
    # N = input()
    
    # # データリスト作成
    # a = [input() for _ in range(N)]

    a = [4,1,3,5,2]
    print(InsertionSort(a))