class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        c=list(zip(*grid))
        n=len((c))

        d=[1]*n

        for i in range(1,n):
            for  j in range(i):
                if all(abs(x-y)<=limit for x,y in zip(c[i],c[j])):
                    d[i]=max(d[i],d[j]+1)
        return max(d)