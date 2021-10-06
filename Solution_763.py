class Solution_763:
    def partitionLabels(self, s: str) -> List[int]:
        startEndPos = {}
        for i, c in enumerate(s):
            if c not in startEndPos:
                startEndPos[c] = [len(s),-1]
            startEndPos[c][0] = min(startEndPos[c][0],i)
            startEndPos[c][1] = max(startEndPos[c][1],i)
        startEndList = sorted(startEndPos.values())
        partitionCandidate = startEndList[0][1] + 1
        result = []
        for start,end in startEndList:
            if start >= partitionCandidate:
                result.append(partitionCandidate)
                partitionCandidate = end + 1
            if end >= partitionCandidate:
                partitionCandidate = end + 1
        result = [0] + result + [len(s)]
        return [result[i] - result[i-1] for i in range(1,len(result))]