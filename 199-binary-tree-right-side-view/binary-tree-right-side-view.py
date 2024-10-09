# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        case 1: All nodes on the right
        case 2: All nodes on the left
        case 3: Nodes are mixed
        Algo:
            nodes = []
            next = []
            since root always in nodes
                add root to next
                add root value to node
            while next:
                for each node in next:
                    add left, right to next
                if next:
                    add last next node value to nodes
            
        '''

        nodes = []
        next_node = deque()
        if root:
            nodes.append(root.val)
            next_node.append(root)

        while next_node:
            n = len(next_node)

            for _ in range(0, n):
                node = next_node.popleft()
                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)
            if next_node:
                nodes.append(next_node[-1].val)
        
        return nodes