class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        sr=0
        er=n-1
        sc=0
        ec=m-1
        result=[]
        while(sr<=er and sc<=ec):
            #left to right
            for i in range(sc,ec+1):
                result.append(matrix[sr][i])
            sr+=1
            #top to bottom
            for i in range(sr,er+1):
                result.append(matrix[i][ec])
            ec-=1
            if sr<=er:
                #right to left
                for i in range(ec,sc-1,-1):
                    result.append(matrix[er][i])
                er-=1
            if(sc<=ec):
            #bottom to top
                for i in range(er,sr-1,-1):
                    result.append(matrix[i][sc])
                sc+=1
        return result

        
