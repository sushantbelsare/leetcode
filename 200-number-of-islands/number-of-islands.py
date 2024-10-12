from collections import OrderedDict

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
                if 0 <= i + dx < m and 0 <= j + dy < n and grid[i + dx][j + dy] == "1":
                    grid[i + dx][j + dy] = "0"
                    dfs(i + dx, j + dy)

        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    num_islands += 1

        return num_islands
