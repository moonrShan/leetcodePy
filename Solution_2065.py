class Solution_2065:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        self.maxTime = maxTime
        self.result = 0
        self.graph = collections.defaultdict(list)
        self.dist = collections.defaultdict(int)
        self.values = values
        for u, v, t in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
            self.dist[(u, v)] = t
        self.dfs(0, 0, set([0]))
        return self.result

    def dfs(self, node, totalTime, visited):
        if totalTime <= self.maxTime:
            if node == 0:
                totalValue = sum([self.values[i] for i in visited])
                self.result = max(self.result, totalValue)
            for child in self.graph[node]:
                if child in visited:
                    self.dfs(child, totalTime + self.dist[(node, child)] + self.dist[(child, node)], visited)
                else:
                    visited.add(child)
                    self.dfs(child, totalTime + self.dist[(node, child)] + self.dist[(child, node)], visited)
                    visited.remove(child)




