class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        self.graph = collections.defaultdict(set)
        self.memo = {}

        for i, prev in enumerate(prevRoom):
            if prev != -1:
                self.graph[prev].add(i)

        return self.dfs(self.graph[0])

    def dfs(self, nextAvaiable):
        if not nextAvaiable:
            return 1
        nextAvaiableTuple = tuple(nextAvaiable)
        if nextAvaiableTuple in self.memo:
            return self.memo[nextAvaiableTuple]
        result = 0
        for nextRoom in list(nextAvaiable):
            nextAvaiable.remove(nextRoom)
            result += self.dfs(nextAvaiable | self.graph[nextRoom])
            nextAvaiable.add(nextRoom)
        self.memo[nextAvaiableTuple] = result
        return result
