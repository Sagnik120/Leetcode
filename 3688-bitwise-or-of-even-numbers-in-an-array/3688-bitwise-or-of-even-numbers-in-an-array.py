class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        flag=0
        ans=0
        for num in nums:
            if num & 1==0:
                ans|=num
        return ans