class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans=0
        if numOnes <= k:
            ans += numOnes
            k -= numOnes

            if numZeros <= k:
                k -= numZeros
                ans -= k
        else:
            return k

        return ans