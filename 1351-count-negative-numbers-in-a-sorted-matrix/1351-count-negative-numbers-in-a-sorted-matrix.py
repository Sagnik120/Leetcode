class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        ans = 0

        for row in grid:

            low = 0
            high = cols - 1

            firstNegative = cols

            while low <= high:

                mid = (low + high) // 2

                if row[mid] < 0:
                    firstNegative = mid
                    high = mid - 1
                else:
                    low = mid + 1

            ans += cols - firstNegative

        return ans