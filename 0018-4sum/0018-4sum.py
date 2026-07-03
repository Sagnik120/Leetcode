class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        i=0
        ans=[]
        while i<len(nums)-3:
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            j=i+1
            while j<len(nums)-2:
                if j>i+1  and nums[j]==nums[j-1]:
                    j+=1
                    continue
                k=j+1
                l=len(nums)-1
                while k < l:
                    s=nums[i]+nums[j]+nums[k]+nums[l]
                    if(s<target):
                        k+=1
                    elif(s>target):
                        l-=1
                    else:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        l-=1
                        k+=1

                        while k<l  and nums[k]==nums[k-1]:
                            k+=1
                        while l>k and nums[l]==nums[l+1]:
                            l-=1
                j+=1
            i+=1
        return ans