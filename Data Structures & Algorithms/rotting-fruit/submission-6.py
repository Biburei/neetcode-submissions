from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, columns =len(grid), len(grid[0])
        islands = deque()
        count = 0
        fresh = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 2:
                    islands.append((row, column))
                elif grid[row][column] == 1:
                    fresh += 1
        if fresh == 0:
            return 0

        while islands and fresh > 0:
            count+=1
            for _ in range(len(islands)):
                r, c = islands.popleft()
                for dir_row, dir_col in directions:
                    new_row, new_col = dir_row + r, dir_col + c
                    if (rows > new_row >= 0 and
                        columns  > new_col >= 0 and
                        grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 2
                        islands.append((new_row, new_col))
                        fresh -= 1
        
        if fresh > 0:
            return -1
        return count

