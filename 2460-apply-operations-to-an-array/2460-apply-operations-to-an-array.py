class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=2*nums[i]
                nums[i+1]=0

        write = 0
        n=len(nums)
        for read in range(n):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        while write < n:
            nums[write] = 0
            write += 1

        return nums