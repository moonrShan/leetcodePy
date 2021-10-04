class Solution_1137:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1
        t0, t1, t2 = 0,1,1
        for i in range(n-2):
            t3 = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = t3
        return t2