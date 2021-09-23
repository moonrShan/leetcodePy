class Solution_753:
    def crackSafe(self, n: int, k: int) -> str:
        self.resultLength = k ** n
        self.visited = set()
        self.result = '0' * (n-1)
        self.dfs(n, k)
        return self.result

    def dfs(self, n: int, k: int) -> bool:
        if len(self.visited) == self.resultLength: return True
        prevString = self.result[-n+1:] if n > 1 else ''

        for c in [str(i) for i in range(k)]:
            nextString = prevString + c
            if nextString not in self.visited:
                self.visited.add(nextString)
                self.result += c
                if self.dfs(n, k):
                    return True
                else:
                    self.visited.remove(nextString);
                    self.result = self.result[:-1]
        return False
def main():
    testObject = Solution_753()
    print(testObject.crackSafe(1,2))

if __name__ == "__main__":
    main()