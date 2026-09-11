class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])
        
        def dfs(row, column, index):
            if index == len(word):
                return True

            if 0 > row or row >= rows or 0 > column or column >= columns or board[row][column] != word[index]:
                return False
            
            node = board[row][column]
            board[row][column] = '#'

            for dir_row, dir_column in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row, new_column = dir_row + row, dir_column + column
                if dfs(new_row, new_column, index + 1):
                    return True
            
            board[row][column] = node
            return False

        for r in range(rows):
            for c in range(columns):
                if dfs(r, c, 0):
                    return True
        return False


