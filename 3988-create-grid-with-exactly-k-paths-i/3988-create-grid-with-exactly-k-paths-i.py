class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        if m==1 and n==1:
            return ["."] if k==1 else []
        g=[[2]*n for _ in range(m)]
        g[0][0]=g[-1][-1]=0
        c=[(i,j) for i in range(m) for j in range(n) if (i,j) not in ((0,0),(m-1,n-1))]
        c.sort(key=lambda p:p[0]+p[1])
        def f(a):
            d=[[0]*n for _  in range(m)]
            d[0][0]=1
            for i in range(m):
                for j in range(n):
                    if not i and not j:
                        continue
                    if g[i][j]==1 or (g[i][j]==2 and not a):
                        continue
                    if i:d[i][j]+=d[i-1][j]
                    if j:d[i][j]+=d[i][j-1]
            return d[-1][-1]
        def dfs(x):
            mi,ma=f(0),f(1)

            if k<mi or k>ma:
                return False
            if mi==k:
                for i in range(x,len(c)):
                    g[c[i][0]][c[i][1]]=1
                return True
            if ma==k:
                for i in range(x,len(c)):
                    g[c[i][0]][c[i][1]]=0
                return True
            r,y=c[x]
            g[r][y]=1
            if dfs(x+1):
                return True
            g[r][y]=0
            if dfs(x+1):
                return True
            g[r][y]=2
            return False
        return ["".join("." if  v==0 else "#" for v in r) for r in g] if dfs(0) else []