class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()

        for i in range(len(nums)-1,-1,-1):
            ans.append(nums[i])
            if sum(ans)>sum(nums[:i]):
                break
        return ans