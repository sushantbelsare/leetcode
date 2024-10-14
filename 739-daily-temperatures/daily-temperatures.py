class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                i = stack.pop()
                res[i] = index - i

            stack.append(index)

        return res