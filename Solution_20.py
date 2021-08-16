class Solution_20:
    def isValid(self, s: str) -> bool:
        stack = []
        pairedParentheses = {'(' : ')', '[' : ']','{' : '}'}
        for parenthes in s:
            if parenthes in pairedParentheses:
                stack.append(parenthes)
            elif stack and pairedParentheses[stack[-1]] == parenthes:
                stack.pop()
            else:
                return False
        return stack == []