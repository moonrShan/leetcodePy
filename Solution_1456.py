class Solution_1456:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        vowelSet = {'a','e','i','o','u'}
        for i in range(k):
            if s[i] in vowelSet:
                res += 1
        p1, p2 = 1, k
        currentRes = res
        while p2 < len(s):
            if s[p1-1] in vowelSet:
                currentRes -= 1
            if s[p2] in vowelSet:
                currentRes += 1
            res = max(currentRes,res)
            p1 += 1
            p2 += 1
        return res