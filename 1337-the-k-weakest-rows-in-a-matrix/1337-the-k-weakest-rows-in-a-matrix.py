class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []

        for i, row in enumerate(mat):
            l, h = 0, len(row) - 1
            soldiers = len(row)

            while l <= h:
                mid = (l + h) // 2

                if row[mid] == 0:
                    soldiers = mid
                    h = mid - 1
                else:
                    l = mid + 1

            rows.append((soldiers, i))

        rows.sort()

        return [idx for _, idx in rows[:k]]