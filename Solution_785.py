class Solution_785:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colored = {}
        for i in range(len(graph)):
            if i not in colored:
                colored[i] = 1
                queue = collections.deque([i])
                while queue:
                    node = queue.popleft()
                    for child in graph[node]:
                        if child not in colored:
                            colored[child] = -colored[node]
                            queue.append(child)
                        elif colored[child] == colored[node]:
                            return False
        return True