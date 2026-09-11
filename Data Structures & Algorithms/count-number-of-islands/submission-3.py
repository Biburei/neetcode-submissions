class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if 0 > r or r >= rows or 0 > c or c >= columns or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'

            for dir_row, dir_column in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(dir_row + r, dir_column + c)


        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == '1':
                    islands += 1
                    dfs(row, column)
        
        return islands