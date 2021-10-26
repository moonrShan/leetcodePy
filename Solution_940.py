class Solution_940:
    def distinctSubseqII(self, s: str) -> int:
        end = [0] * 26
        for c in s:
            end[ord(c) - ord('a')] = sum(end) + 1
        return sum(end) % (10**9 + 7)