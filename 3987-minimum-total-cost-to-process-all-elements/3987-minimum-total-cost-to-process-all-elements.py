class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        r,c,o,m=k,0,0,10**9+7
        for x in nums:
            if x>r:
                p=(x-r+k-1)//k
                e=(o+p)
                c=(c+e*(e+1)//2-o*(o+1)//2)%m
                o,r=e,r+p*k
            r-=x
        return c
        