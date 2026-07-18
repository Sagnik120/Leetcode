class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        res = []
        odd_ind = []
        even_ind = []
        for i in range(1,n,2):
            odd_ind.append(nums[i])
        for i in range(0,n-1,2):
            even_ind.append(nums[i])
        for i in range(n//2):
            res.append(odd_ind[i])
            res.append(even_ind[i])

        return res