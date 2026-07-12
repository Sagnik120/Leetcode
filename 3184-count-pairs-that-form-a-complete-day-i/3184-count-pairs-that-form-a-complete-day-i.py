class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        frq=[0]*24
        ans=0


        for h in hours:
            rem=h%24
            ans+=frq[(24-rem)%24]
            frq[rem]+=1
        return ans