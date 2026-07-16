class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
     
        product1 = nums[0] * nums[1] * nums[2]
        
        product2 = nums[0] * nums[-1] * nums[-2]
        
        return max(product1, product2)