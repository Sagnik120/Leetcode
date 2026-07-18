class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        
        # 2. Convert to a sorted list in descending order
        sorted_nums = sorted(list(unique_nums), reverse=True)
        
        # 3. Check if we have at least 3 distinct elements
        if len(sorted_nums) >= 3:
            return sorted_nums[2]
        
        # 4. Otherwise, return the maximum element
        return sorted_nums[0]

