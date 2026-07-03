class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low=0
        high=len(nums)-1
        

        while high>=low:
            mid=low+((high-low)>>1)
            if nums[mid]==target:
                return True
            
            # if all the low,mid,high values are same
            if(nums[low]==nums[mid]==nums[high]):
                high-=1
                low+=1
                continue
            
            # left half sorted
            if nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            
            # right half is sorted
            else:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            
        return False