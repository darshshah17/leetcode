# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def getHeight(self, root):
#         # height of a node = depth of the same node assuming that
#         # node to be the root
#         if not root:
#             return 0

#         return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         # unrelated note: depth = root -> specific node
#         #                 height = specific node -> leaf

#         # my soln (O(n^2) time):
#         # make a fcn (node (ptr) --> height) (dfs)
#         # use cache (memoization) to save memory

#         # then, do either dfs or bfs to compare the height
#         # of both children of each node using the map
#         if not root:
#             return True

#         stack = [root]

#         while stack:
#             node = stack.pop()

#             if node.left:
#                 stack.append(node.left)
#             if node.right:
#                 stack.append(node.right)

        
#         stack = [root]

#         while stack:
#             node = stack.pop()

#             leftHeight = self.getHeight(node.left)
#             rightHeight = self.getHeight(node.right)

#             if abs(leftHeight - rightHeight) > 1:
#                 return False

#             if node.left:
#                 stack.append(node.left)
#             if node.right:
#                 stack.append(node.right)


#         return True

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # previous soln is O(n^2), this is O(n). The difference
        # is that this is bottom up, so it doesn't require the 
        # redundant calculation of height for each subtree of the
        # overall tree, since it can simply be found from the max of
        # the height of the children.

        # this is one of the problems i'm trying to do with recursion
        # instead of iteratively bc the soln is much more difficult
        # the other way, usually its not.

        # this is not my soln (my soln is above).
        # returns 2 values (if the subtree is balanced and its height)
        def dfs(node):
            if not node:
                return [True, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            return [
                left[0] and right[0] and abs(left[1] - right[1]) <= 1,
                1 + max(left[1], right[1])
            ]

        return dfs(root)[0]