class Solution_1881:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == '-':
            for i,c in enumerate(n[1:]):
                if x < int(c):
                    return n[:i+1] + str(x) + n[i+1:]
        else:
            for i,c in enumerate(n):
                if x > int(c):
                    return n[:i] + str(x) + n[i:]
        return n+str(x)