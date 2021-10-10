class Solution_529:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.dfs(board, click[0], click[1])
        return board

    def dfs(self, board, i, j):
        d = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
        m, n = len(board), len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return
        if board[i][j] == 'E':
            mine = 0
            for x, y in d:
                if 0 <= i + x < m and 0 <= j + y < n:
                    mine += board[i + x][j + y] == 'M'
            if mine:
                board[i][j] = str(mine)
                return
            board[i][j] = 'B'
            for x, y in d:
                self.dfs(board, i + x, j + y)
        return

