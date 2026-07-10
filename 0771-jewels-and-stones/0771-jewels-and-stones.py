class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        frq={}

        for s in stones:
            frq[s]=frq.get(s,0)+1
        ans=0
        for s in jewels:
            if s in frq:
                ans+=frq[s]
        return ans