class Solution_370:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length
        for update in updates:
            start, end, inc = update
            res[start] += inc
            if end + 1 <= length - 1:
                res[end+1] -= inc
        currSum = 0
        for i in range(length):
            currSum += res[i]
            res[i] = currSum
        return res