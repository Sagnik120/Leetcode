class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans=1
        for i in range(len(nums)):
            if nums[i]<0:
                ans*=-1
            elif nums[i]>0:
                ans*=1
            else:
                return 0
        return ans