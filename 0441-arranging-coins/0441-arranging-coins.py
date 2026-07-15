class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans=0
        count=1
        while n>=0:
            n-=count
            ans+=1
            count+=1
        return ans-1