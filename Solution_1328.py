class Solution_1328:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1: return ""
        middle = len(palindrome) // 2
        for i, c in enumerate(palindrome[:middle]):
            if c != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b'