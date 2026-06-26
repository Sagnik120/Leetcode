class Solution:
    def minChanges(self, n: int, k: int) -> int:
        count = 0

        while n > 0 or k > 0:
            nb = n & 1
            kb = k & 1

            if nb == 0 and kb == 1:
                return -1

            if nb == 1 and kb == 0:
                count += 1

            n >>= 1
            k >>= 1

        return count
