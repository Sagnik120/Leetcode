class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        INT_MAX=float("-inf")
        pre=1
        suf=1
        for i in range(0,len(nums)):
            if pre==0: 
                pre=1
            if suf==0: 
                suf=1
            pre*=nums[i]
            suf*=nums[len(nums)-1-i]

            INT_MAX = max(INT_MAX, pre, suf)
            
        return INT_MAX             