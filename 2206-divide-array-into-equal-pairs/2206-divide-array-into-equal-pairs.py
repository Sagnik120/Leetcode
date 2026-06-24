class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        set1=set()

        for num in nums:
            if num in set1:
                set1.remove(num)
            else:
                set1.add(num)
        return len(set1)==0
