from typing import List


class Solution_344:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i,n = 0, len(s)
        while i < n // 2:
            temp = s[i]
            s[i] = s[n - i - 1]
            s[n - i - 1] = temp
            i += 1