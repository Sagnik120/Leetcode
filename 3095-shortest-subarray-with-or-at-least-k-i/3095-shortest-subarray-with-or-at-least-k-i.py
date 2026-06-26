class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min1=float('inf')
        for i in range(len(nums)):
            sum1=0
            for j in range(i,len(nums)):
                sum1 |=nums[j]
                if(sum1>=k):
                    min1=min(min1,j-i+1)
        return -1 if min1 == float("inf") else min1