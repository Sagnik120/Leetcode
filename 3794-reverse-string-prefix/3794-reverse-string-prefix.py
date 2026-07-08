class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        d=list(s)
        low=0
        high=k-1
        while high>=low:
            d[low],d[high]=d[high],d[low]
            low+=1
            high-=1
        return "".join(d)