from collections import deque
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = deque()
        for c in s:
            if not stack or stack[-1] + c != "()":
                stack.append(c)
            else:
                stack.pop()

        return len(stack)

        
        