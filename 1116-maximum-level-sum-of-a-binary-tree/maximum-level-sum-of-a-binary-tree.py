# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''
        default lowest level will always be 1
        first node to traverse will always start root i.e. next_node[0] = root
        Algo:
            1. next_node = { root }
            2. set sum = 0, current_level = 1, final_level = 1
            3. for each node in next_node:
            4.      add value to temporary sum
            5.      add node to next_node
            6.      update current_level = current_level + 1
            7. if temporary sum > final sum
            8.      sum = temporary sum
            9.      final_level = current_level
            10. repeat steps 3 to 7 until there's no next node
            11. return final_level
        '''

        next_node = deque()
        next_node.append(root)
        current_level = final_level = 1
        max_sum = root.val
        while next_node:
            n = len(next_node)
            current_sum = 0
            for _ in range(0, n):
                node = next_node.popleft()
                if node.left:
                    next_node.append(node.left)
                    current_sum += node.left.val
                if node.right:
                    next_node.append(node.right)
                    current_sum += node.right.val
            if next_node:
                current_level += 1
                if current_sum > max_sum:
                    max_sum = current_sum
                    final_level = current_level

        return final_level
        