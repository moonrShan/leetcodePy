class Solution_2062:
    def countVowelSubstrings(self, word: str) -> int:
        return self.atMost(word, 5) - self.atMost(word, 4)

    def atMost(self, s, goal):
        result = 0
        left = 0
        n = len(s)
        counter = collections.Counter()
        for right in range(len(s)):
            if s[right] not in "aeiou":
                left = right + 1
                counter.clear()
                continue
            counter[s[right]] += 1
            while len(counter) > goal:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            result += right - left + 1
        return result
