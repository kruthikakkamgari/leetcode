
class Solution:
    def dfs(self, i, j, image, pos, new_color, n, m):
        image[i][j] = new_color
        for row, col in [[-1,0],[1,0],[0,-1],[0,1]]:
            delRow = i + row
            delCol = j + col
            if (0 <= delRow < n and 0 <= delCol < m and image[delRow][delCol] == pos):
                self.dfs(delRow, delCol, image, pos, new_color, n, m)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        visited=[]
        for i in range(n):
            temp=[0]*m
            visited.append(temp)
            pos = image[sr][sc]
            if pos == color:
                return image
            self.dfs(sr, sc, image, pos, color, n, m)
        return image
