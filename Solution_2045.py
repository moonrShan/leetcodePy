class Solution_2045:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = collections.defaultdict(list)
        queue = collections.deque([1])
        totalTime = 0

        while queue:
            if (totalTime // change) % 2:
                totalTime += (totalTime // change + 1) * change - totalTime
            totalTime += time
            for i in range(len(queue)):
                node = queue.popleft()
                for child in graph[node]:
                    if child == n and len(visited[child]) == 1 and visited[child][0] != totalTime:
                        return totalTime
                    if (len(visited[child]) == 0) or (len(visited[child]) == 1 and visited[child][0] != totalTime):
                        queue.append(child)
                        visited[child].append(totalTime)


