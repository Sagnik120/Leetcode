class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        min1=float('inf')
        while high>=low:
            mid=low+((high-low)>>1)
            # left half  sorted
            if nums[mid]>=nums[low]:
                min1=min(min1,nums[low])
                low=mid+1
            #right half is sorted
            else:
                min1=min(min1,nums[mid])
                high=mid-1
        return min1
