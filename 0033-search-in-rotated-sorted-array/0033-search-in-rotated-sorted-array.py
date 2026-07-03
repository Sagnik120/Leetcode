class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1

        while high>=low:
            mid=low+((high-low)>>1)
            if nums[mid]==target:
                return mid
            #left half is sorted
            if nums[mid]>=nums[low]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            
            #right half is sorted
            else:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1