class Solution_39:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        candidates = sorted(candidates)
        currentCombine = []
        for i in range(len(candidates)):
            currentCombine.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, currentCombine)
            currentCombine.pop()
        return self.result

    def dfs(self, candidates, target, startIndex, currentCombine):
        if target == 0:
            self.result.append(list(currentCombine))
            return
        if target < 0:
            return
        for i in range(startIndex, len(candidates)):
            currentCombine.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, currentCombine)
            currentCombine.pop()