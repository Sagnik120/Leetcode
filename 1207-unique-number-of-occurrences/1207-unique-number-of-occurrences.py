class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frq={}
        for num in arr:
            frq[num]=frq.get(num,0)+1
        s=set()
        for key in frq:
            s.add(frq[key])
        return len(s)==len(frq)