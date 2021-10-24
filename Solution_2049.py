class Solution_2049:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        self.graph = collections.defaultdict(list)
        self.children = collections.defaultdict(list)
        for i in range(len(parents)):
            if parents[i] >= 0:
                self.graph[parents[i]].append(i)
        self.dfsCountChildren(0)

        result = 1
        total = len(parents)
        for i in range(len(parents)):
            [left,right]= self.children[i]
            result = max(result, max(left, 1) * max(right, 1) * max(total - left - right - 1, 1))

        return result

    def dfsCountChildren(self, node):
        child = self.graph[node]
        if not child or len(child) == 0:
            self.children[node] = [0, 0]
        if len(child) == 1:
            self.children[node] = [1 + self.dfsCountChildren(child[0]), 0]
        if len(child) == 2:
            self.children[node] = [1 + self.dfsCountChildren(child[0]), 1 + self.dfsCountChildren(child[1])]
        return sum(self.children[node])
