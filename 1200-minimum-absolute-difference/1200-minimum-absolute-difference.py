class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        A = arr[:] 
        A.sort()
        n = len(A)
        minDiff = float('inf') # A bit cleaner than 2e6 + 1
        res = []

        for i in range(1, n):
            diff = A[i] - A[i - 1]
            if diff < minDiff:
                minDiff = diff
                res = [[A[i - 1], A[i]]]
            elif diff == minDiff:
                res.append([A[i - 1], A[i]])

        return res