class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = -1
        second_max = -1
        max_idx = -1
        
        # Single pass to find the largest and second largest elements
        for i, num in enumerate(nums):
            if num > max_val:
                second_max = max_val  # Old max becomes the second max
                max_val = num
                max_idx = i
            elif num > second_max:
                second_max = num
                
        # Check if the largest is at least twice the second largest
        if max_val >= 2 * second_max:
            return max_idx
            
        return -1