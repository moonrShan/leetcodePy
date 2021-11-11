class Solution_140:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.result = []
        self.potentialCutLength = list(set([len(word) for word in wordDict]))
        self.wordDict = set(wordDict)
        currentCut = []
        for cut in self.potentialCutLength:
            if s[:cut] in self.wordDict:
                currentCut.append(s[:cut])
                self.dfs(s[cut:],currentCut)
                currentCut.pop()
        return self.result

    def dfs(self,s,currentCut):
        if not s:
            self.result.append(" ".join(currentCut))
            return
        for cut in self.potentialCutLength:
            if cut <= len(s) and s[:cut] in self.wordDict:
                currentCut.append(s[:cut])
                self.dfs(s[cut:],currentCut)
                currentCut.pop()
        return