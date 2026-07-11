class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        frq={}
        for num in nums:
            frq[num]=frq.get(num,0)+1

        for num in nums:
            if num & 1==0 and frq[num]==1:
                return num
        return -1