class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frq=Counter(arr)
        m=-1
        for num in arr:
            if frq[num]==num:
                m=max(m,num)
        return m