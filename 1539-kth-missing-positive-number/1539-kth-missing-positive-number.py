class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums=[]
        i=1
        for num in arr:
            while i<num:
                nums.append(i)
                i+=1
            i+=1
        while len(nums) < k:
            nums.append(i)
            i += 1

        return nums[k - 1]        