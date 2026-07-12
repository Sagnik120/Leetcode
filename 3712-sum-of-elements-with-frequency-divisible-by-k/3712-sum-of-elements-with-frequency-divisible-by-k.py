class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        frq=Counter(nums)
        s=0
        for key in frq:
            if frq[key]%k==0:
                s+=key*frq[key]
        return s  