class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        def canMake(day):
            flowers = 0
            bouquets = 0

            for bloom in bloomDay:

                if bloom <= day:
                    flowers += 1
                else:
                    bouquets += flowers // k
                    flowers = 0

            bouquets += flowers // k

            return bouquets >= m


        low=min(bloomDay)
        high=max(bloomDay)

        while high>=low:
            mid=low+((high-low)>>1)
            if canMake(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
