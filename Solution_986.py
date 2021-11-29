class Solution_986:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = 0
        second = 0
        result = []
        while first < len(firstList) and second < len(secondList):
            firstStart, firstEnd = firstList[first]
            secondStart, secondEnd = secondList[second]
            interStart = max(firstStart,secondStart)
            interEnd = min(firstEnd,secondEnd)
            if interStart <= interEnd:
                result.append([interStart,interEnd])
            if firstEnd < secondEnd:
                first += 1
            else:
                second += 1
        return result