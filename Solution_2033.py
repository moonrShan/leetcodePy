class Solution_2033:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        elements = []
        for i in range(m):
            elements += grid[i]
        elements = sorted(elements)
        return self.help(elements, elements[m * n // 2], x)

    def help(self, elements, target, x):
        totalDifference = 0
        for element in elements:
            difference = abs(target - element)
            if difference % x: return - 1
            totalDifference += difference

        return totalDifference // x
