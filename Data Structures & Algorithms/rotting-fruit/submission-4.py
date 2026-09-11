from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        rotten = deque()
        rows, columns = len(grid), len(grid[0])
        fresh = 0
        minutes = 0

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    rotten.append((row, column))
                elif grid[row][column] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        while rotten and fresh > 0:
            for _ in range(len(rotten)):
                row, column = rotten.popleft()
                for drow, dcolumn in directions:
                    new_row, new_column = drow + row, dcolumn + column
                    if (rows > new_row >= 0 and
                        columns > new_column >= 0 and
                        grid[new_row][new_column] == 1):
                            grid[new_row][new_column] = 2
                            fresh -= 1
                            rotten.append([new_row, new_column])
            minutes += 1
                    
        if fresh == 0:
            return minutes
        return -1