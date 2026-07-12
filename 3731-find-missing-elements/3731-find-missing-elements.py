class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l=min(nums)
        h=max(nums)
        
        ans=[]

        for i in range(l,h+1):
            if i not in nums:
                ans.append(i)

        return ans