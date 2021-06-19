# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode):
        if not root: return None
        
        def toLeft(node):
            if not node: return None
            res.append(toLeft(node.left))
            res.append(toLeft(node.right))

            return node.val
        res = []
        return res

node = TreeNode()
root = [5,3,6,2,4,None,8,1,None,None,None,7,9]
for i in range(0, len(root)-2):
    node.val(root[root(i)])
    node.left(root[root(i*2+1)])
    node.right(root[root(i*2+2)])
