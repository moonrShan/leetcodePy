class Solution_1997:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        visited = collections.defaultdict(int)
        currentRoom = 0
        visited[currentRoom] += 1
        result = 0
        while len(visited) < n:
            if visited[currentRoom] % 2:
                currentRoom = nextVisit[currentRoom]
            else:
                currentRoom = (currentRoom + 1) % n
            visited[currentRoom] += 1
            result += 1
        return result