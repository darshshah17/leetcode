# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # not my soln (O(h) where h = height of tree):
        
        # compare their values (since its a BST)
        # if both p and q are greater or smaller than the current root,
        # it cannot be the least common ancestor (it can be an ancestor, 
        # just not the least). The LCA is the one that has p/q in
        # either the left/right subtree, and the other in the other subtree
        
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
        