class Solution_1488:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dic = collections.defaultdict(list)
        ret = [-1] * len(rains)
        to_empty = []  # index
        full = set([])
        for day, lake in enumerate(rains):
            dic[lake].append(day)

        for i in range(len(rains)):
            lake = rains[i]
            if lake:
                if lake in full:
                    return []
                full.add(lake)
                dic[lake].pop(0)
                if dic[lake]:
                    heapq.heappush(to_empty, dic[lake][0])
            else:
                if to_empty:
                    ret[i] = rains[heapq.heappop(to_empty)]
                    full.remove(ret[i])
                else:
                    ret[i] = 1
        return ret