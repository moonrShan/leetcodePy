class Solution_2059:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        self.visited = set()
        queue = collections.deque([start])
        step = 0
        while queue:
            for i in range(len(queue)):
                value = queue.popleft()
                if value == goal:
                    return step
                if not (value < 0 or value > 1000):
                    for child in self.createNext(value, nums):
                        queue.append(child)
            step += 1
        return - 1

    def createNext(self, parent, nums):
        result = []
        for num in nums:
            child = parent + num
            if child not in self.visited:
                result.append(child)
                self.visited.add(child)

            child = parent - num
            if child not in self.visited:
                result.append(child)
                self.visited.add(child)

            child = parent ^ num
            if child not in self.visited:
                result.append(child)
                self.visited.add(child)
        return result