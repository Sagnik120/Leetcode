class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i,num in enumerate(nums):
            ans ^=num
        return ans

        