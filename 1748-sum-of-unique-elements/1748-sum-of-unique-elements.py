class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        frq={}
        for num in nums:
            frq[num]=frq.get(num,0)+1
        s=0
        for key in frq:
            if frq[key]==1:
                s+=key
        return s