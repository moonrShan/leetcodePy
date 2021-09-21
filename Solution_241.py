class Solution_241:
    def __init__(self):
        self.memo = {}  # expression string -> list result

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression in self.memo:
            return self.memo[expression]
        result = []
        nums = 0;
        operatorSet = {'+', '-', '*'};
        for i, c in enumerate(expression):
            if c in operatorSet:
                leftGroup = self.diffWaysToCompute(expression[:i])
                rightGroup = self.diffWaysToCompute(expression[i + 1:])
                for left in leftGroup:
                    for right in rightGroup:
                        if c == '+':
                            result.append(left + right)
                        elif c == '-':
                            result.append(left - right)
                        elif c == '*':
                            result.append(left * right)
            else:
                nums = nums * 10 + int(c)
        if not result:
            result = [nums]
        self.memo[expression] = result
        return result