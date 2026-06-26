class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        flag=0
        for num in nums:
            if num & 1==0:
                flag+=1
            if(flag>=2):
                return True
        return False