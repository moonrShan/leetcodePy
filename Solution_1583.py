class Solution_1583:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        candidate = {}
        for x, y in pairs:
            candidate[x] = preferences[x][:preferences[x].index(y)]
            candidate[y] = preferences[y][:preferences[y].index(x)]

        result = 0
        for x in candidate:
            for y in candidate[x]:
                if x in candidate[y]:
                    result += 1
                    break
        return result