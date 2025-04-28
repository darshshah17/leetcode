# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        stack = [(p, q)]
        while stack:
            nodeP, nodeQ = stack.pop()

            if nodeP and nodeQ:
                if nodeP.val != nodeQ.val:
                    return False
            else:
                if nodeP and not nodeQ or not nodeP and nodeQ:
                    return False

            
            if (nodeP.left == None) != (nodeQ.left == None) or (nodeP.right == None) != (nodeQ.right == None):
                return False
            
            if nodeP.left:
                stack.append((nodeP.left, nodeQ.left))
            if nodeP.right:
                stack.append((nodeP.right, nodeQ.right))

        return True