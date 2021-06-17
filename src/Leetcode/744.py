from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        N = len(letters)
        for i in range(N):
            if ord(letters[i]) > ord(target):
                return letters[i]
            elif ord(letters[i]) == ord(target) and i < N-1:
                if ord(letters[i+1]) == ord(target): continue
                return letters[i+1]
        return letters[0]
sol = Solution()
print(sol.nextGreatestLetter(["c", "f", "j"], "j"))
print(sol.nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"], "e"))
print(sol.nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"], "n"))