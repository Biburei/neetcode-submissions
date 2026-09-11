from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        cnt = 0
        islands = deque()
        rows, columns = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    islands.append((r, c))
                    grid[r][c] = '0'
                    cnt += 1
                    while islands:
                        row, column = islands.popleft()
                        for dir_row, dir_col in directions:
                            new_row, new_column = row + dir_row, column + dir_col
                            if (rows > new_row >=0 and
                                columns > new_column >= 0 and
                                grid[new_row][new_column] == "1"):
                                islands.append((new_row, new_column))
                                grid[new_row][new_column] = '0'
        return cnt
