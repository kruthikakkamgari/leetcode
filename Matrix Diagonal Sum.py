class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        mid=n//2
        for i in range(n):
            ans += mat[i][i] + mat[i][n - i - 1]
        if n % 2 == 1:
            ans -= mat[mid][mid]
        return ans
