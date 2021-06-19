class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # base case
        if not root: return
        
        sum = 0
        if root.val >= low and root.val <= high:
            sum += root.val
        self.rangeSumBST(root.left, low, high)
        self.rangeSumBST(root.right, low, high)
        
        return sum

sol = Solution()
print(sol.rangeSumBST(TreeNode([10,5,15,3,7,None,18]), 7, 15))