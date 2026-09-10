from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        horizontal, vertical = len(grid), len(grid[0])
        rotten = deque()
        cnt = 0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    cnt += 1
        minutes = 0
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while rotten and cnt > 0:
            minutes += 1

            for _ in range(len(rotten)):
                row ,column = rotten.popleft()
                for nxt_row, nxt_column in direction:
                    delta_column = column + nxt_column
                    delta_row = row + nxt_row

                    if (vertical > delta_column >= 0
                        and horizontal > delta_row >= 0 
                        and grid[delta_row][delta_column] == 1):

                        grid[delta_row][delta_column] = 2
                        rotten.append([delta_row, delta_column])
                        cnt -= 1
                    if cnt == 0:
                        return minutes
        return -1 if cnt > 0 else 0