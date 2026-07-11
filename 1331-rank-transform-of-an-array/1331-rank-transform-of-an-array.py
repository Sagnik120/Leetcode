class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        nums=arr[:]
        nums.sort()
        frq={}
        count=1
        for i in range(0,len(nums)-1):
            if nums[i]!=nums[i+1]:
                frq[nums[i]]=count
                count+=1
            else:
                frq[nums[i]]=count
        frq[nums[len(nums)-1]]=count
        result=[]
        for num in arr:
            result.append(frq[num])
        return result
