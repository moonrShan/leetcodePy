class Solution_8:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        maxInt = 2 ** 31 - 1
        minInt = -2 ** 31
        sign = 1
        index = 0
        if s[index] == '-' or s[index] == '+':
            if s[index] == '-':
                sign = -1
            index += 1
        num = 0
        while index < len(s):
            if not s[index].isdigit(): break
            if maxInt // 10 < num or maxInt // 10 == num and maxInt % 10 < int(s[index]):
                return maxInt if sign == 1 else minInt
            num = num * 10 + int(s[index])
            index += 1

        return num * sign