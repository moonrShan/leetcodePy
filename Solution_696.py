class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        consecutiveList = []
        previous = None
        currCount = 0
        for c in s:
            if c == "0":
                if previous == "0" or not previous:
                    currCount += 1
                else:
                    consecutiveList.append(currCount)
                    currCount = 1
                previous = "0"

            if c == "1":
                if previous == "1" or not previous:
                    currCount += 1
                else:
                    consecutiveList.append(currCount)
                    currCount = 1
                previous = "1"
        consecutiveList.append(currCount)
        res = 0
        for i in range(1, len(consecutiveList)):
            res += min(consecutiveList[i - 1], consecutiveList[i])
        return res