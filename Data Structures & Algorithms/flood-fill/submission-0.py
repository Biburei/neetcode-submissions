class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, columns = len(image), len(image[0])
        original = image[sr][sc]
        if original == color:
            return image

        def dfs(r, c, original):

            if 0 > r or r >= rows or 0 > c or c >= columns or image[r][c] != original:
                return image
            
            image[r][c] = color
                        
            for dir_r, dir_c in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(dir_r + r, dir_c + c, original)
            return image

        return dfs(sr, sc, original)
        
