# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root: return root
        return self.recurse(root, None)
    
    def recurse(self, root, tail):
        if not root: return tail
        res = self.recurse(root.left, root)
        root.left = None
        root.right = self.recurse(root.right, tail)

        return res

