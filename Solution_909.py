class Solution_909:
    def snakesAndLadders(self, board):
        n = len(board)
        need = {1: 0}
        bfs = [1]
        for x in bfs:
            refuse_steps = False
            for i in range(min(n**2, x + 6), x, -1):
                a, b = (i - 1) // n, (i - 1) % n
                nxt = board[~a][b if a % 2 == 0 else ~b]
                if nxt > 0: i = nxt
                if i == n * n: return need[x] + 1
                if nxt == -1 and refuse_steps: continue
                if nxt == -1: refuse_steps = True
                if i not in need:
                    need[i] = need[x] + 1
                    bfs.append(i)
        return -1