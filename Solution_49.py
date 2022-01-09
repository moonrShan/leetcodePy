import collections
from typing import List


class Solution_49:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultDict = collections.defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            resultDict[key].append(s)
        return list(resultDict.values())