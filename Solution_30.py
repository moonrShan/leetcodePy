class Solution_30:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLength = len(words[0])
        result = []
        counter = collections.Counter(words)
        for i in range(len(s) - wordLength + 1):
            if self.dfs(s,i,wordLength,dict(counter)):
                result.append(i)
        return result

    def dfs(self,s,pos,wordLength,counter):
        if not counter:
            return True
        if pos + wordLength > len(s):
            return False
        word = s[pos:pos+wordLength]
        if word not in counter:
            return False
        counter[word] -= 1
        if counter[word] == 0:
            del counter[word]
        return self.dfs(s,pos+wordLength,wordLength,counter)