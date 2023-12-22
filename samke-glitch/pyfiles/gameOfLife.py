from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])

        directions = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)]
        def countLiveNeighbors(x, y):
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and abs(board[nx][ny]) == 1:
                    count += 1
            return count
        
        for i in range(m):
            for j in range(n):
                liveNeighbors = countLiveNeighbors(i, j)
                if board[i][j] == 1:
                    if liveNeighbors < 2 or liveNeighbors > 3:
                        board[i][j] = -1
                else:
                    if liveNeighbors == 3:
                        board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        
