class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # pair_cnt = 0
        # pair = []
        # for rl in s:
        #     if len(pair) == 0:
        #         pair.append(rl)
        #     elif pair[-1] == rl:
        #         pair.append(rl)
        #     elif pair[-1] != rl and len(pair) > 0:
        #         pair.pop(0)
        #     else:
        #         pair = []

        #     if len(pair) == 0:
        #         pair_cnt += 1

        # return pair_cnt
        cnt = 0
        res = 0
        for c in s:
            if c == "L":
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                res += 1
                cnt = 0

        return res
        