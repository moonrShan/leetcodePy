class Solution_1275:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows, cols = [0] * n, [0] * n
        diag, antiDiag = 0, 0
        player = 1
        for x, y in moves:
            rows[x] += player
            cols[y] += player
            if x == y:
                diag += player
            if x + y == n - 1:
                antiDiag += player

            if any(abs(line) == n for line in (rows[x], cols[y], diag, antiDiag)):
                return "A" if player == 1 else "B"
            player *= -1

        return "Draw" if len(moves) == n * n else "Pending"