class Solution:
    def reverseByType(self, s: str) -> str:
        r=len(s)-1
        l=0

        nums=list(s)


        while l<r:
            while l<r and not nums[l].isalnum():
                l+=1
            while  l<r and not nums[r].isalnum():
                r-=1
            
            if l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        r=len(s)-1
        l=0
        while l<r:
            while l<r and nums[l].isalnum():
                l+=1
            while  l<r and nums[r].isalnum():
                r-=1
            
            if l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        
        return "".join(nums)
