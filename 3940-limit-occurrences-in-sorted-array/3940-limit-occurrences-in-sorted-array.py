class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        if len(nums)==1:
            return nums
        ans=[]
        ans = [nums[0]]
        count=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                count+=1
                if count<=k:
                    ans.append(nums[i])
            else:
                ans.append(nums[i])
                count=1
        return ans