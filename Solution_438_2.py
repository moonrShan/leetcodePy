class Solution_438_2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        counter = collections.Counter(p)
        for i in range(len(s)):
            counter[s[i]] -= 1
            left = i-len(p)+1
            if left >= 0:
                if all([v == 0 for k,v in counter.items()]):
                    result.append(i-len(p)+1)
                counter[s[left]] += 1
        return result
