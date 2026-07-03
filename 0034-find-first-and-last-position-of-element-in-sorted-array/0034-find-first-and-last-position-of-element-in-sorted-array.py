class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        a=-1
        while high>=low:
            mid=low+((high-low)>>1)
            if nums[mid]>=target:
                a=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
        if a == -1 or nums[a] != target:
            return [-1, -1]

        low=0
        high=len(nums)-1
        b=-1
        while high>=low:
            mid=low+((high-low)>>1)
            if nums[mid]<=target:
                b=mid
                low=mid+1
                
            elif nums[mid]>target:
                high=mid-1
       
        return [a,b]