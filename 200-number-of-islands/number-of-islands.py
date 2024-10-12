from collections import OrderedDict

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j, visited):
            for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
                if 0 <= i + dx < m and 0 <= j + dy < n and (i + dx, j + dy) not in visited and grid[i + dx][j + dy] == "1":
                    visited.add((i + dx, j + dy))
                    dfs(i + dx, j + dy, visited)

        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j, visited)
                    num_islands += 1

        return num_islands
