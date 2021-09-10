from typing import List


class Solution_848:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(shifts)
        for i in range(n-2,-1,-1):
            shifts[i] = shifts[i] + shifts[i + 1]
        result = ''
        for i in range(n):
            result +=  (chr)((ord(s[i]) + shifts[i] - ord('a')) % 26 + ord('a'))
        return result