class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max1=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(abs(nums[i]-nums[j])<=min(nums[i],nums[j])):
                    max1=max(max1,nums[i]^nums[j])
        return max1