from collections import deque


class Solution_127:
    def ladderLength(self, beginWord, endWord, wordList):
        wordListSet = set(wordList)
        queue = deque([[beginWord,1]])
        while queue:
            word,step = queue.popleft()
            if word == endWord:
                return step
            for c in "abcdefghijklmnopqrstuvwxyz":
                for i in range(len(word)):
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordListSet:
                        wordListSet.remove(newWord)
                        queue.append([newWord,step+1])
        return 0