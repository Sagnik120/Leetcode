class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1

        while high>low:
            mid=low+((high-low)>>1)
            if nums[mid]<nums[mid+1]:
                low=mid+1
            else:
                high=mid
        return low
