class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        frq={}
        for num in deck:
            frq[num]=frq.get(num,0)+1
        g=0
        for count in frq.values():
            g=gcd(g, count)
        return g>=2