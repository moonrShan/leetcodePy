class TicTacToe:

    def __init__(self, n: int):
        self.judge = [0] * (2 * n + 2)
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.judge[row] += 1
            self.judge[self.n + col] += 1
            if row == col:
                self.judge[2 * self.n] += 1
            if row + col == self.n - 1:
                self.judge[2 * self.n + 1] += 1
        else:
            self.judge[row] -= 1
            self.judge[self.n + col] -= 1
            if row == col:
                self.judge[2 * self.n] -= 1
            if row + col == self.n - 1:
                self.judge[2 * self.n + 1] -= 1
        if any([abs(x) == self.n for x in self.judge]):
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)