class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        even=0
        odd=1
        for num in nums:
            if num & 1==0:
                arr[even]=num
                even+=2
            else:
                arr[odd]=num
                odd+=2
        return arr
        