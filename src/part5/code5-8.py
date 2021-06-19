INF = 20000000

def chmin(a, b):
    if a > b: return b
    return a

def main(S: str, T: str):
    """
    1. subproblems:
        Sのi文字分とTのj文字分までの編集距離
        空白 = algorithm
        空白 = xxxxxxxxx
        編集距離=9
        l = algorithm
        l = xoxxxxxxx
        編集距離=8
        log = algorithm
        log = xoooxxxxx
        編集距離=7(goの変換が入る)
    2. recurrece relations:
        今回は最小値を求めるため小さい値を採用する
        def chmin(a, b):
            if a > b: return b
            return a
        x = 0
        for i in range(len(S) + 1):
            for j in range(len(T) + 1):
                if i > 0 and j > 0:
                    # 残す
                    if S[i - 1] == T[j - 1] : x = x
                    # 変更
                    else: i > 0 and j > 0: x += 1
                # 追加
                if i > 0: x += 1
                # 削除
                if j > 0: x += 1

    """
    # DPテーブル定義
    dp = [[INF for _ in range(len(T)+1)] for _ in range(len(S)+1)]
    # 初期条件設定
    dp[0][0] = 0
    # DPループ
    for i in range(0, len(S)+1):
        for j in range(0, len(T)+1):
            # 変更操作
            if i > 0 and j > 0:
                if S[i-1] == T[j-1]:
                    dp[i][j] = chmin(dp[i][j], dp[i - 1][j - 1])
                else:
                    dp[i][j] = chmin(dp[i][j], dp[i - 1][j - 1] + 1)

            # 削除操作
            if i > 0: dp[i][j] = chmin(dp[i][j], dp[i - 1][j] + 1)

            # 挿入操作
            if j > 0: dp[i][j] = chmin(dp[i][j], dp[i][j-1] + 1)

    return dp[len(S)][len(T)]
            

    
if __name__ == "__main__":
    S = 'logistic'
    T = 'algorithm'

    print(main(S, T))
