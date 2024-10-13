# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node == None:
                return None

            l = dfs(node.left)
            m = dfs(node.right)

            if node == p or node == q or (l == p and m == q) or (l == q and m == p):
                return node
                
            return l or m

        return dfs(root)
            


