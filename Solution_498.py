import collections


class Solution_498:
    def findDiagonalOrder(self, matrix):
        result = [ ]
        dd = collections.defaultdict(list)
        if not matrix: return result
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                dd[i+j+1].append(matrix[i][j])
        for k in sorted(dd.keys()):
            if k%2==1: dd[k].reverse()
            result += dd[k]
        return result