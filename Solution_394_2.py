class Solution_394_2:
    def decodeString(self, s: str) -> str:
        stack, currentNum, currentString = [], 0, ''
        for c in s:
            if c.isalpha():
                currentString += c
            elif c.isdigit():
                currentNum = currentNum * 10 + int(c)
            elif c == '[':
                stack.append(currentString)
                stack.append(currentNum)
                currentString = ''
                currentNum = 0
            elif c == ']':
                prevNum = stack.pop()
                prevString = stack.pop()
                currentString = prevString + prevNum * currentString
        return currentString