# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter of the tree must be the max (sum of the left
        # and right height) across all subtrees

        # Not my soln (O(n))
        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            heightLeft = dfs(node.left)
            heightRight = dfs(node.right)

            res = max(res, heightLeft + heightRight)

            return 1 + max(heightLeft, heightRight)

        dfs(root)
        return res