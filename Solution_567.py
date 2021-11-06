class Solution_567:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import collections
        counter = collections.Counter(s1)
        left = 0
        for right in range(len(s2)):
            counter[s2[right]] -= 1
            while counter[s2[right]] < 0:
                counter[s2[left]] += 1
                left += 1
            if all([v == 0 for k, v in counter.items()]):
                return True
        return False


