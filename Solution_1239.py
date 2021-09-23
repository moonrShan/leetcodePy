class Solution_1239:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for a in arr:
            if len(a) != len(set(a)): continue
            a = set(a)
            for c in dp:
                if a & c: continue
                dp.append(a | c)
        return max(len(c) for c in dp)