class Solution:
    def isSubsequence(self, s, t) -> bool:
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
print(sol.isSubsequence([1,2,5], [1,2,3,4]))