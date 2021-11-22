class Solution_2073:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = [[x,i] for i,x in enumerate(tickets)]
        queue = collections.deque(queue)
        totalTime = 0
        while queue:
            cur = queue.popleft()
            nextCur = [cur[0]-1,cur[1]]
            totalTime += 1
            if nextCur[0] == 0 and nextCur[1] == k:
                return totalTime
            elif nextCur[0] > 0:
                queue.append(nextCur)