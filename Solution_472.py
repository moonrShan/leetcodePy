from typing import List


class Solution_472:
    def __init__(self):
        self.result = []

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if len(words) < 3: return []
        words = sorted(words, key=lambda x: len(x))
        for i, word in enumerate(words):
            self.dfs(word, '', set(words[:i]))
        return self.result

    def dfs(self, target, current, candidates):
        if target == current:
            self.result.append(target)
            return
        for candidate in candidates:
            nextCurrent = current + candidate
            if nextCurrent == target[:len(nextCurrent)]:
                self.dfs(target, nextCurrent, candidates)



