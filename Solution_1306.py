

class Solution_1306:
    def canReach(self, arr: List[int], start: int) -> bool:
        return self.dfs(arr, start)

    def dfs(self, arr, pos):
        if pos < 0 or pos > len(arr) - 1 or arr[pos] == '#': return False
        if arr[pos] == 0: return True
        step = arr[pos]
        arr[pos] = '#'
        return self.dfs(arr, pos + step) or self.dfs(arr, pos - step)