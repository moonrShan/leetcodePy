from typing import List


class Solution_378:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        resultList = matrix[0]
        for i in range(1, n):
            resultList = self.merge(resultList, matrix[i])
        return resultList[k - 1]

    def merge(self, listA, listB):
        p1 = 0
        p2 = 0
        n1 = len(listA)
        n2 = len(listB)
        result = []
        while p1 < n1 and p2 < n2:
            if listA[p1] <= listB[p2]:
                result.append(listA[p1])
                p1 += 1
            else:
                result.append(listB[p2])
                p2 += 1
        if p1 == n1:
            result += listB[p2:]
        if p2 == n2:
            result += listA[p1:]
        return result
