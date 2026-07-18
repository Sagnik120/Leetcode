class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        bits = 0
        k=original
        for num in nums:
            q, r = divmod(num, k)
            if r == 0 and (q & (q - 1)) == 0:
                bits |= q
        n = bits + 1
        return k * (n & -n)