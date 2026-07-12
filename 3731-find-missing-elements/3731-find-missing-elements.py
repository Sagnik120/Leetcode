class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l=min(nums)
        h=max(nums)

        frq={}

        for num in nums:
            frq[num]=1
        
        ans=[]

        for i in range(l,h+1):
            if i not in frq:
                ans.append(i)

        return ans