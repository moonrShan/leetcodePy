class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        res = []
        preWords = set()
        words.sort(key=len)

        for word in words:
            if self.wordBreak(word, preWords):
                res.append(word)
            preWords.add(word)

        return res

    def wordBreak(self, string, words):
        if not words:
            return False

        dp = [False] * (len(string) + 1)
        dp[0] = True

        for i in range(len(string) + 1):
            for j in range(i):
                if dp[j] and string[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]