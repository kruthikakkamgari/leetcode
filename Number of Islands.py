class Solution:
    def dfs(self,i,j,grid,visited,n,m):
        visited[i][j]=1
        for row,col in [[-1,0],[1,0],[0,-1],[0,1]]:
            delRow=i+row
            delCol=j+col
            if(delRow>=0 and delRow<n and delCol>=0 and delCol<m  and grid[delRow][delCol]=="1" and visited[delRow][delCol]==0):
                self.dfs(delRow,delCol,grid,visited,n,m)

    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visited=[]
        for i in range(n):
            temp=[0]*m
            visited.append(temp)
        count=0
        for i in range(n):
            for j in range(m):
                if (grid[i][j]=='1' and visited[i][j]==0):
                    self.dfs(i,j,grid,visited,n,m)
                    count+=1
        return count


        
