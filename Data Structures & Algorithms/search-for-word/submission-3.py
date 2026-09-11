class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])

        def dfs(r, c, index):

            if index == len(word):
                return True

            if 0 > r or r  >= rows or 0 > c or c >= columns or board[r][c] != word[index]:
                return False
                
            temporary = board[r][c]
            board[r][c] = "%"

            for dir_row, dir_column in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_row, next_column = dir_row + r, dir_column + c
                if dfs(next_row, next_column, index + 1):
                    return True
            
            board[r][c] = temporary
            return False
        
        for r in range(rows):
            for c in range(columns):
                if dfs(r, c, 0):
                    return True
                    
        return False


