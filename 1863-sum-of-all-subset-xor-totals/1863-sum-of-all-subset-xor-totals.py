class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=0

        def dfs(i,xor_val):
            nonlocal ans

            if i==len(nums):
                ans+=xor_val
                return
            
            #don't take
            dfs(i+1,xor_val)

            #take
            dfs(i+1,xor_val^nums[i])

        dfs(0,0)
        return ans