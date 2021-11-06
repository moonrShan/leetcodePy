class Solution_438:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        counter = collections.Counter(p)
        for c in s[:len(p) - 1]:
            counter[c] -= 1
        for i in range(len(p)-1,len(s)):
            counter[s[i]] -= 1
            if all([v == 0 for k,v in counter.items()]):
                result.append(i-len(p)+1)
            counter[s[i-len(p)+1]] += 1
        return result
