class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frq={}
        for num in nums:
            frq[num]=frq.get(num,0)+1
            if frq[num]>len(nums)>>1:
                return num