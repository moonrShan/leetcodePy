class Solution_2045_2:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        dis1, dis2 = [float("inf")] * (n + 1), [float("inf")] * (n + 1)
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dis1[1] = 0
        q = deque()
        q.append((0, 1))
        while q:
            cost, node = q.popleft()
            for nei in graph[node]:
                nxt_cost = cost + time;
                if (cost // change) % 2 == 1:
                    nxt_cost += change - (cost % change)
                if dis1[nei] > nxt_cost:
                    dis2[nei], dis1[nei] = dis1[nei], nxt_cost;
                    q.append((nxt_cost, nei))
                elif nxt_cost > dis1[nei] and nxt_cost < dis2[nei]:
                    dis2[nei] = nxt_cost
                    q.append((nxt_cost, nei))
        return dis2[n]


