class Solution_898:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        dp = []
        for num in arr:
            if not dp:
                dp.append(set([num]))
            else:
                lastResult = dp[-1]
                curResult = set([num])
                for x in lastResult:
                    curResult.add(x | num)
                dp.append(curResult)
        result = set()
        for subresult in dp:
            for x in subresult:
                result.add(x)
        return len(result)

