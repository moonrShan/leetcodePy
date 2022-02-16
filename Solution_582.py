import collections
from typing import List


class Solution_582:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = collections.defaultdict(list)
        for i, parent in enumerate(ppid):
            graph[parent].append(pid[i])

        queue = collections.deque([kill])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            queue += graph[node]
        return result