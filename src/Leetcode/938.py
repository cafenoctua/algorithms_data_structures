# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        total = 0

        if root.val > high:
            total = self.rangeSumBST(root.left, low, high)
        elif root.val < low:
            total = self.rangeSumBST(root.right, low, high)
        else:
            total = root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        return total
sol = Solution()
print(sol.rangeSumBST(TreeNode([10,5,15,3,7,None,18]), 7, 15))
print(sol.rangeSumBST([10,5,15,3,7,13,18,1,None,6], 6, 10)) 