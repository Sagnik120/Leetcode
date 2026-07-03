class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans=-1
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1