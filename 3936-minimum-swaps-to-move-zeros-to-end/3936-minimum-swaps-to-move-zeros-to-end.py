class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        left=0
        right=len(nums)-1
        ans=0
        while right>left:
            while nums[right]==0 and left < right:
                right-=1

            while nums[left]!=0 and left < right:
                left+=1
    
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                ans += 1
                left += 1
                right -= 1
        return ans