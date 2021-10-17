class Solution_2042:
    def areNumbersAscending(self, s: str) -> bool:
        previousNum = -1
        num = 0
        for c in s + " ":
            if c.isdigit():
                num = num * 10 + int(c)
            if c == " " and num > 0:
                if num <= previousNum:
                    return False
                previousNum = num
                num = 0
        return True