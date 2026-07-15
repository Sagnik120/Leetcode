class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, h = 0, n

        while l <= h:
            mid = (l + h) // 2
            coins = mid * (mid + 1) // 2

            if coins <= n:
                l = mid + 1
            else:
                h = mid - 1

        return h