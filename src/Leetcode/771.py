class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         cnt = 0
#         for jewel in jewels:
#             for stone in stones:
#                 if stone == jewel:
#                     cnt += 1
                    
#         return cnt
        # cnt = 0
        # a = [0 for i in jewels for j in stones if i == j]
        # return len(a)
        a = map(jewels.count, stones)
        return map(jewels.count, stones)


solution = Solution()
print(solution.numJewelsInStones("aA", "aAAAzzzz"))