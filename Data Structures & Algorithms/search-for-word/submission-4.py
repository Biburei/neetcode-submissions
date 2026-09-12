class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])

        def dfs(r, c, index):
            if index == len(word):
                return True

            if 0 > r or r >= rows or 0 > c or c >= columns or board[r][c] != word[index]:
                return False

            temporary = board[r][c]
            board[r][c] = '!'

            for dir_r , dir_c in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_r, new_c = dir_r + r, dir_c + c
                if dfs(new_r, new_c, index + 1):
                    return True
            board[r][c] = temporary
            return False

        for row in range(rows):
            for column in range(columns):
                if dfs(row, column, 0):
                    return True
        return False