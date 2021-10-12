class Solution_79:
    def exist(self, board, word):
        self.visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if  word[0]== board[i][j]:
                    self.visited.add((i,j))
                    if self.dfs(board, i, j, word[1:]):
                        return True
                    self.visited.remove((i,j))
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0: return True
        for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
            newx, newy = i + dx, j + dy
            if  0 <= newx < len(board) and 0 <= newy < len(board[0]) and word[0] == board[newx][newy] and (newx,newy) not in self.visited:
                self.visited.add((newx,newy))
                if self.dfs(board, newx, newy, word[1:]):
                    return True
                self.visited.remove((newx,newy))
        return False