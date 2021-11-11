class Solution_339:
    def depthSum(self, nestedList):
        return self.depthSum(nestedList,1)

    def depthSum(self, nestedList, currentDepth):
        result = 0
        for sums in nestedList:
            if isinstance(sums, list):
                result += self.depthSum(nestedList,currentDepth + 1)
            else:
                result += currentDepth * sums
        return result