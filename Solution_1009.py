class Solution_1009:
    def bitwiseComplement(self, n: int) -> int:
        if not n:
            return 1
        bitlist = []
        while n:
            bitlist.append(1 - n % 2)
            n = n >> 1
        return sum([2 ** i * x for i, x in enumerate(bitlist)])
