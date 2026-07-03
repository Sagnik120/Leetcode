class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        low = 0
        high = cols - 1

        while low <= high:

            mid = (low + high) // 2

            # Find the row with the maximum element in mid column
            maxRow = 0
            for r in range(rows):
                if mat[r][mid] > mat[maxRow][mid]:
                    maxRow = r

            left = mat[maxRow][mid - 1] if mid > 0 else -1
            right = mat[maxRow][mid + 1] if mid < cols - 1 else -1

            if mat[maxRow][mid] > left and mat[maxRow][mid] > right:
                return [maxRow, mid]

            elif left > mat[maxRow][mid]:
                high = mid - 1

            else:
                low = mid + 1