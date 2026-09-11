from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, columns = len(grid), len(grid[0])
        count = 0
        islands = deque()

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == '1':
                    islands.append((row, column))
                    count += 1
                    while islands:
                        row, column = islands.popleft()
                        for dir_row, dir_column in directions:
                            new_row, new_column = row + dir_row, column + dir_column
                            if(rows > new_row >= 0 and
                                columns > new_column >= 0 and
                                grid[new_row][new_column] == '1'):
                                islands.append((new_row, new_column))
                                grid[new_row][new_column] = '0'
        return count

                           
