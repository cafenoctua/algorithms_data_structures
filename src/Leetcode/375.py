def guess(num: int):
    n = 3 - num
    if n == 0: return 0
    elif n >0 : return 1
    else: return -1

class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(n)==0: return n
        r = n
        l = 0
        c = int((r + l)/2)
        res = guess(c)
        while res != 0:
            if res == 1:
                l = c
            elif res == -1:
                r = c
            c = int((r + l) / 2)
            res = guess(c)
        return c

sol = Solution()
print(sol.guessNumber(3))