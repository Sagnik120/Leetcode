class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        frq={}
        r=0
        while n!=0:
            r=n%10
            frq[r]=frq.get(r,0)+1
            n=n//10
        ans=0
        for key in frq:
            ans+=key*frq[key]

        return ans