class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        maxArea = 0
        islands = []

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    islands.append((r, c))

        def dfs(r, c) -> int:

            if 0 > r or r >= rows or 0 > c or c >= columns or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = 1

            for dir_row, dir_column in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                area += dfs(dir_row + r, dir_column + c)
                    
            return area

        for r in range(rows):
            for c in range(columns):
                maxArea = max(maxArea, dfs(r, c))
        return maxArea
