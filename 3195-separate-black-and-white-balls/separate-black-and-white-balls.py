class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        steps = i = ones = 0
        while i < n:
            zeros = 0
            while i < n and s[i] == "1":
                ones += 1
                i += 1
            while i < n and s[i] == "0":
                zeros += 1
                i += 1

            steps += ones * zeros

        return steps
