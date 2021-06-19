class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        for letter in s:
            # print(t)
            if letter not in t:
                return False
            else:
                print(letter)
        return True
sol = Solution()
# print(sol.isSubsequence("abc", "ahbgdc"))
print(sol.isSubsequence("aaaaaa", "bbaaaa"))