class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        n=len(mat)-1
        for i in range(len(mat)):
            s+=mat[i][i]
            if i!=n:
                s+=mat[i][n]
            n-=1
        return s