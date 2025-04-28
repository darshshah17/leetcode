# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSame(self, currRoot, subRoot):
        if not currRoot and not subRoot:
            return True
        if not currRoot or not subRoot:
            return False

        stack = [(currRoot, subRoot)]

        while stack:
            node1, node2 = stack.pop()

            if node1 and node2:
                if node1.val != node2.val:
                    return False
            else:
                if not node1 and not node2:
                    return True
                elif node1 or node2:
                    return False
            
            if (node1.left == None) != (node2.left == None) or (node1.right == None) != (node2.right == None):
                return False
            
            if node1.left:
                stack.append((node1.left, node2.left))
            if node1.right:
                stack.append((node1.right, node2.right))

        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        while stack:
            node = stack.pop()

            if node.val == subRoot.val and self.isSame(node, subRoot):
                return True

            if node and node.left:
                stack.append(node.left)
            if node and node.right:
                stack.append(node.right)

        return False
        