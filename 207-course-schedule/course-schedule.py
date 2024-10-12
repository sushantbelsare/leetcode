class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for i, j in prerequisites:
            adj_list[j].append(i)
            indegree[i] += 1

        ans = []

        queue = deque()

        for i in range(0, numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            t = queue.popleft()
            ans.append(t)
            for i in adj_list[t]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        return len(ans) == numCourses
